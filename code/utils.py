import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np
from aind_data_schema.core.quality_control import (QCMetric, QCStatus, Stage,
                                                   Status)
from aind_data_schema_models.modalities import Modality
from pynwb import NWBFile
from scipy.stats import gaussian_kde

status_pending = QCStatus(
    evaluator="", status=Status.PENDING, timestamp=datetime.now()
)

status_pass = QCStatus(
    evaluator="", status=Status.PASS, timestamp=datetime.now()
)

status_fail = QCStatus(
    evaluator="", status=Status.FAIL, timestamp=datetime.now()
)


def get_running_velocity_qc_metric(
    nwb: NWBFile, output_path: Path, threshold: float
) -> Dict[str, List[QCMetric]]:
    """
    Gets the running velocity from the processed nwb

    Parameters
    ----------
    nwb: NWBFile
        The processed nwb file

    output_path: Path
        Output directory where figures are to be saved

    threshold: float
        The threshold to check if values are lower than this

    Returns
    -------
    Dict[str, List[QCMetric]]
        Dictionary with qc metrics
    """
    metric_name = "Running Velocity"
    running_data = nwb.processing["behavior"].data_interfaces["Encoder"]
    data = running_data.data[:]
    velocity_average = float(np.nanmean(data))
    if velocity_average < 0 or velocity_average > threshold:
        status = status_fail
    else:
        status = status_pass

    qc_metric = QCMetric(
        name=metric_name,
        value={"Average": velocity_average},
        description=str(
            f"Fail when Average {metric_name} is "
            f"below 0 or above {threshold}"
        ),
        status_history=[status],
        tags=[metric_name],
        modality=Modality.BEHAVIOR,
        stage=Stage.PROCESSING,
    )

    return {metric_name: [qc_metric]}


def get_general_performance_qc_metrics(
    nwb: NWBFile, output_path: Path
) -> Dict[str, List[QCMetric]]:
    """
    Gets the general performance metrics from the processed nwb

    Parameters
    ----------
    nwb: NWBFile
        The processed nwb file

    output_path: Path
        Output directory where figures are to be saved

    Returns
    -------
    Dict[str, List[QCMetric]]
        Dictionary with qc metrics
    """
    metric_name = "General Performance"
    events = nwb.get_events__events_tables().to_dataframe()

    total_rewards = len(events[events["event_name"] == "GiveReward"])
    total_patches = (
        events[events["event_name"] == "ActivePatch"]["event_data"]
        .unique()
        .size
    )

    if total_patches == 0 or total_rewards == 0:
        status = status_fail
    else:
        status = status_pass

    qc_metric = QCMetric(
        name=metric_name,
        value={
            "Total Rewards": total_rewards,
            "Total Patches": total_patches,
        },
        description=str(
            f"Fail {metric_name}: When any metrics have value 0.",
        ),
        status_history=[status],
        tags=[metric_name],
        modality=Modality.BEHAVIOR,
        stage=Stage.PROCESSING,
    )

    return {metric_name: [qc_metric]}
