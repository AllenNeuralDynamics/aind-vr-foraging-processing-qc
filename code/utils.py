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

status_pass = QCStatus(
    evaluator="", status=Status.PASS, timestamp=datetime.now()
)

status_fail = QCStatus(
    evaluator="", status=Status.FAIL, timestamp=datetime.now()
)

# user defined environment threshold to fail
ENVIRONMENT_THRESHOLD = (23, 28)

# user defined velocity threshold to fail
VELOCITY_THRESHOLD = 70

# user defined lick density threshold to fail
LICK_DENSITY_THRESHOLD = 0.1

# user defined number of licks threshold to fail
NUMBER_OF_LICKS_THRESHOLD = 1000

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
        if average < ENVIRONMENT_THRESHOLD[0] or average > ENVIRONMENT_THRESHOLD[1]:
            status = status_fail
        else:
            status = status_pass

        fig, ax = plt.subplots()
        ax.plot(sensor_data["Time"], sensor_data[metric_name])
        ax.set_xlabel("Time (s)")
        ax.set_ylabel(metric_name)
        ax.set_title(f"Environment - {metric_name}")

        fig.savefig(output_path / f"environment_{metric_name}.png")
        qc_metric = QCMetric(
            name=f"Environment - {metric_name}",
            value={"Average": average},
            reference=f"environment_{metric_name}.png",
            description=str(
                f"Rule to fail is if Average {metric_name} is below "
                f"{ENVIRONMENT_THRESHOLD[0]} or is above "
                f"{ENVIRONMENT_THRESHOLD[1]}. Otherwise pass."
            ),
            status_history=[status],
            
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
    running_data = nwb.processing["behavior"].data_interfaces["Encoder"]
    data = running_data.data[:]
    velocity_average = float(np.nanmean(data))
    if velocity_average < 0 or velocity_average > VELOCITY_THRESHOLD:
        status = status_fail
    else:
        status = status_pass

    qc_metric = QCMetric(
        name=metric_name,
        value={"Average": velocity_average},
        description=str(
            f"Rule to fail if Average {metric_name} is "
            f"below 0 or above {VELOCITY_THRESHOLD}"
        ),
        status_history=[status],
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
            f"Rule for failing {metric_name}: If any metrics have value 0, "
            f"fail. Otherwise pass.",
        ),
        status_history=[status],
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
    if len(inter_licks_distribution) > 1:
        kde = gaussian_kde(inter_licks_distribution)
        x = np.linspace(0, max(inter_licks_distribution), 500)
        density = kde(x)

        below_mask = density < LICK_DENSITY_THRESHOLD
        count_below = np.sum(below_mask)
        proportion_below = count_below / len(density)

        if proportion_below < LICK_DENSITY_THRESHOLD:
            status = status_fail
        else:
            status = status_pass

        ax.plot(x, density)
        ax.axhline(0.1, color="r", linestyle="--")
        ax.set_xlabel("Inter-lick interval (s)")
        ax.set_ylabel("Density")
        ax.set_title("Inter-licks Distribution")
        fig.savefig(output_path / "inter_licks_distribution.png")
        qc_metric_inter_licks_distribution = QCMetric(
            name="Inter-licks distribution",
            value=None,
            reference="inter_licks_distribution.png",
            description=str(
                f"Rule for failing. If density < "
                f"{LICK_DENSITY_THRESHOLD}. Otherwise pass."
            ),
            status_history=[status],
        )
        metrics[metric_name].append(qc_metric_inter_licks_distribution)

    number_of_licks = len(licks[licks["event_data"]])
    if number_of_licks == 0 or number_of_licks > NUMBER_OF_LICKS_THRESHOLD:
        status = status_fail
    else:
        status = status_pass

    qc_metric_lick_count = QCMetric(
        name="Number of licks",
        value={"Number of licks": number_of_licks},
        description=str(
            "Rule for failing. If number of licks is 0 or "
            f"above {NUMBER_OF_LICKS_THRESHOLD}. Otherwise pass"
        ),
        status_history=[status],
    )
    metrics[metric_name].append(qc_metric_lick_count)

    # offset - onset
    lick_onset_offset = nwb.acquisition["Behavior.HarpLickometer.LickState"][:]
    onsets = lick_onset_offset.loc[
        lick_onset_offset["Channel0"], "Time"
    ].reset_index(drop=True)
    offsets = lick_onset_offset.loc[
        ~lick_onset_offset["Channel0"], "Time"
    ].reset_index(drop=True)

    durations = onsets - offsets
    lick_variability_within = np.nanstd(durations)

    # Plot histogram
    fig, ax = plt.subplots()
    ax.hist(durations, bins=30, alpha=0.7, edgecolor="black")

    # Mark mean
    mean_dur = np.mean(durations)
    ax.axvline(
        mean_dur, color="blue", linestyle="--", label=f"Mean = {mean_dur:.3f}s"
    )

    ax.set_xlabel("Lick duration (s)")
    ax.set_ylabel("Count")
    ax.set_title("Within-lick Duration Distribution (Onset - Offset)")
    ax.set_xlim((0, 200))
    ax.legend()
    fig.savefig(output_path / "licks.png")

    # TODO: get threshold for failing if larger
    qc_metric_within_lick_distribution = QCMetric(
        name="Within lick variability (onset - offset)",
        value={
            "Within lick variability (onset - offset)": float(
                lick_variability_within
            )
        },
        reference="licks.png",
        description="Within lick variability",
        status_history=[status_pending],
    )
    metrics[metric_name].append(qc_metric_within_lick_distribution)

    return metrics
