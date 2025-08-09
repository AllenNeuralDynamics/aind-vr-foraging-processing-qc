import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np
from aind_data_schema.core.quality_control import QCMetric, QCStatus, Status
from pynwb import NWBFile
from scipy.stats import gaussian_kde

status_pending = QCStatus(
    evaluator="", status=Status.PENDING, timestamp=datetime.now()
)


def get_environment_qc_metrics(
    nwb: NWBFile, output_path: Path
) -> Dict[str, List[QCMetric]]:
    """
    Gets qc metrics for envrionmental conditions

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
    qc_metrics = {"Enviornmental Conditions": []}
    sensor_data = nwb.acquisition["Behavior.HarpEnvironmentSensor.SensorData"][
        :
    ]

    for metric_name in ("Temperature", "Humidity"):
        average = float(sensor_data[metric_name].mean())

        fig, ax = plt.subplots()
        ax.plot(sensor_data["Time"], sensor_data[metric_name])
        ax.set_xlabel("Time (s)")
        ax.set_ylabel(metric_name)
        ax.set_title(f"Environment - {metric_name}")

        fig.savefig(output_path / f"environment_{metric_name}.png")
        qc_metric = QCMetric(
            name=f"Environment - {metric_name}",
            value={"Average": average},
            reference=f"/environment_{metric_name}.png",
            description=metric_name,
            status_history=[status_pending],
        )
        qc_metrics["Enviornmental Conditions"].append(qc_metric)

    return qc_metrics


def get_running_velocity_qc_metric(
    nwb: NWBFile, output_path: Path
) -> Dict[str, List[QCMetric]]:
    """
    Gets the running velocity from the processed nwb

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
    metric_name = "Running Velocity"
    running_data = nwb.processing["behavior"].data_interfaces["Treadmill"]
    data = running_data.data[:]

    qc_metric = QCMetric(
        name=metric_name,
        value={"Average": float(np.nanmean(data))},
        description=metric_name,
        status_history=[status_pending],
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

    qc_metric = QCMetric(
        name=metric_name,
        value={
            "Total Rewards": total_rewards,
            "Total Patches": total_patches,
        },
        description=metric_name,
        status_history=[status_pending],
    )

    return {metric_name: [qc_metric]}


def get_lick_qc_metrics(
    nwb: NWBFile, output_path: Path
) -> Dict[str, List[QCMetric]]:
    """
    Gets the lick metrics from the processed nwb

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
    metric_name = "Licks"
    metrics = {metric_name: []}

    events = nwb.get_events__events_tables().to_dataframe()
    events["event_data"] = events["event_data"].apply(json.loads)
    licks = events[events["event_name"] == "Lick"]
    licks["event_data"] = licks["event_data"].astype(bool)

    fig, ax = plt.subplots()
    inter_licks_distribution = np.diff(licks[licks["event_data"]]["timestamp"])
    # KDE
    kde = gaussian_kde(inter_licks_distribution)
    x = np.linspace(0, max(inter_licks_distribution), 500)
    density = kde(x)

    ax.plot(x, density)
    ax.axhline(0.1, color="r", linestyle="--")
    ax.set_xlabel("Inter-lick interval (s)")
    ax.set_ylabel("Density")
    ax.set_title("Inter-licks Distribution")
    fig.savefig(output_path / "inter_licks_distribution.png")
    qc_metric_inter_licks_distribution = QCMetric(
        name="Inter-licks distribution",
        value=None,
        reference="/inter_licks_distribution.png",
        description="Inter-licks distribution",
        status_history=[status_pending],
    )
    metrics[metric_name].append(qc_metric_inter_licks_distribution)

    qc_metric_lick_count = QCMetric(
        name="Number of licks",
        value={"Number of licks": len(licks[licks["event_data"]])},
        description="Number of licks",
        status_history=[status_pending],
    )
    metrics[metric_name].append(qc_metric_lick_count)

    # offset - onset
    lick_variability_within = len(licks[~licks["event_data"]]) - len(
        licks[licks["event_data"]]
    )

    qc_metric_within_lick_distribution = QCMetric(
        name="Within lick variability (offset - onset)",
        value={
            "Within lick variability (offset - onset)": np.std(
                lick_variability_within
            )
        },
        description="Within lick variability",
        status_history=[status_pending],
    )
    metrics[metric_name].append(qc_metric_within_lick_distribution)

    return metrics
