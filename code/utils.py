import matplotlib.pyplot as plt
from pynwb import NWBFile
from aind_data_schema.core.quality_control import QCMetric, QCStatus, Status
from pathlib import Path
from typing import Dict, List
from datetime import datetime
import numpy as np

status_pending = QCStatus(evaluator="", status=Status.PENDING, timestamp=datetime.now())

def get_environment_qc_metrics(nwb: NWBFile, output_path: Path) -> Dict[str, List[QCMetric]]:
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
    sensor_data = nwb.acquisition["Behavior.HarpEnvironmentSensor.SensorData"][:]

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
            status_history=[status_pending]
        )
        qc_metrics["Enviornmental Conditions"].append(qc_metric)
    
    return qc_metrics

def get_running_velocity_qc_metric(nwb: NWBFile, output_path: Path) -> Dict[str, List[QCMetric]]:
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
    timestamps = running_data.timestamps[:]
    data = running_data.data[:]


    qc_metric = QCMetric(
        name=metric_name,
        value={"Average": float(np.nanmean(data))},
        description=metric_name,
        status_history=[status_pending]
    )

    return {metric_name: [qc_metric]}





