import json
import logging
from pathlib import Path

from aind_data_schema.core.quality_control import QualityControl
from hdmf_zarr import NWBZarrIO
from pydantic import Field
from pydantic_settings import BaseSettings

import utils

logger = logging.getLogger(__name__)


class VRForagingSettings(BaseSettings, cli_parse_args=True):
    """
    Settings for VR Foraging Primary Data NWB Packaging
    """

    input_directory: Path = Field(
        default=Path("/data/vr_foraging_processed_nwb"),
        description="Directory where data is",
    )
    output_directory: Path = Field(
        default=Path("/results/"), description="Output directory"
    )
    environment_threshold_low: float = Field(
        default=23,
        description=str(
            "Threshold to check if metric is " "lower than this, than fails",
        ),
    )
    environment_threshold_high: float = Field(
        default=28,
        description=str(
            "Threshold to check if metric is " "higher than this, than fails",
        ),
    )
    velocity_threshold: float = Field(
        default=70,
        description=str(
            "Threshold to check if metric is " "higher than this, than fails",
        ),
    )
    lick_density_threshold: float = Field(
        default=0.1,
        description=str(
            "Threshold to check if metric is " "lower than this, than fails",
        ),
    )
    number_of_licks_threshold: float = Field(
        default=1000,
        description=str(
            "Threshold to check if metric is " "higher than this, than fails",
        ),
    )


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    settings = VRForagingSettings()
    logger.info(f"Settings: {settings}")
    paths = tuple(settings.input_directory.glob("*"))
    processed_nwb_path = [path for path in paths if path.is_dir()]

    if not processed_nwb_path:
        raise FileNotFoundError("No processed nwb found")

    logger.info(f"Found processed nwb at path {processed_nwb_path[0]}")
    with NWBZarrIO(processed_nwb_path[0].as_posix(), "r") as io:
        nwb = io.read()

    logger.info("Computing environment condition metrics")
    environment_metrics = utils.get_environment_qc_metrics(
        nwb,
        settings.output_directory,
        settings.environment_threshold_low,
        settings.environment_threshold_high,
    )

    logger.info("Computing running velocity metrics")
    running_velocity_metric = utils.get_running_velocity_qc_metric(
        nwb, settings.output_directory, settings.velocity_threshold
    )

    logger.info("Computing general peformance metrics")
    general_performance_metrics = utils.get_general_performance_qc_metrics(
        nwb, settings.output_directory
    )

    logger.info("Computing lick metrics")
    lick_metrics = utils.get_lick_qc_metrics(
        nwb,
        settings.output_directory,
        settings.lick_density_threshold,
        settings.number_of_licks_threshold,
    )

    qc_metrics = []
    qc_tags = set()

    for name, metrics in environment_metrics.items():
        qc_metrics.extend(metrics)
        qc_tags.add(name)

    for name, metrics in running_velocity_metric.items():
        qc_metrics.extend(metrics)
        qc_tags.add(name)

    for name, metrics in general_performance_metrics.items():
        qc_metrics.extend(metrics)
        qc_tags.add(name)

    for name, metrics in lick_metrics.items():
        qc_metrics.extend(metrics)
        qc_tags.add(name)

    with open(settings.input_directory.parent / "raw_qc.json", "r") as f:
        raw_qc = json.load(f)

    for metric in QualityControl(**raw_qc).metrics:
        qc_metrics.append(metric)
        for tag in metric.tags:
            qc_tags.add(tag)

    quality_control = QualityControl(
        metrics=qc_metrics, default_grouping=list(qc_tags)
    )
    with open(settings.output_directory / "quality_control.json", "w") as f:
        f.write(quality_control.model_dump_json(indent=4))
