# aind-vr-foraging-processing-qc

This [capsule](https://codeocean.allenneuraldynamics.org/capsule/3338802/tree) generate qc metrics for the VR-Foraging task. The input to this capsule is a **`NWB`** file, and the output of this [capsule](https://codeocean.allenneuraldynamics.org/capsule/5107215/tree), which packages the processed data. 
See [readme](https://github.com/AllenNeuralDynamics/aind-vr-foraging-processing-nwb-packaging) for more details on processed NWB.

### Input
The processed NWB file has 3 main modules that are used for generating qc metrics. They are **`acquisition`**, **`events`**, and **`processing`**. From these modules, qc metrics are calculated - see `utils.py` for more information on implementation. 

### Output
Currently, the output includes metrics and plots related to environment conditions, licks, and general peformance. In addition, a **`quality_control`**.json file is included that adheres to the metadata schema defined [here](https://github.com/AllenNeuralDynamics/aind-data-schema). The quality control json integrates metrics and plots and follows the schema. In addition, it combines it with the quality contorl json from the primary qc capsule (see [readme](https://github.com/AllenNeuralDynamics/aind-vr-foraging-primary-qc) for more details. Sample output of quality control json is below.

```json
{
    "describedBy": "https://raw.githubusercontent.com/AllenNeuralDynamics/aind-data-schema/main/src/aind_data_schema/core/quality_control.py",
    "schema_version": "1.2.2",
    "evaluations": [
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Processing",
            "name": "Enviornmental Conditions",
            "description": "Enviornmental Conditions",
            "metrics": [
                {
                    "name": "Environment - Temperature",
                    "value": {
                        "Average": 28.345388412475586
                    },
                    "status_history": [
                        {
                            "evaluator": "",
                            "status": "Fail",
                            "timestamp": "2025-08-14T21:28:27.573245Z"
                        }
                    ],
                    "description": "Fail when Average Temperature is below 23.0 or is above 28.0.",
                    "reference": "environment_Temperature.png",
                    "evaluated_assets": null
                },
                {
                    "name": "Environment - Humidity",
                    "value": {
                        "Average": 18.480369567871094
                    },
                    "status_history": [
                        {
                            "evaluator": "",
                            "status": "Fail",
                            "timestamp": "2025-08-14T21:28:27.573245Z"
                        }
                    ],
                    "description": "Fail when Average Humidity is below 23.0 or is above 28.0.",
                    "reference": "environment_Humidity.png",
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Fail",
            "created": "2025-08-14T21:28:36.356332Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Processing",
            "name": "Running Velocity",
            "description": "Running Velocity",
            "metrics": [
                {
                    "name": "Running Velocity",
                    "value": {
                        "Average": 14.425584857762935
                    },
                    "status_history": [
                        {
                            "evaluator": "",
                            "status": "Pass",
                            "timestamp": "2025-08-14T21:28:27.572760Z"
                        }
                    ],
                    "description": "Fail when Average Running Velocity is below 0 or above 70.0",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Pass",
            "created": "2025-08-14T21:28:36.356403Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Processing",
            "name": "General Performance",
            "description": "General Performance",
            "metrics": [
                {
                    "name": "General Performance",
                    "value": {
                        "Total Rewards": 230,
                        "Total Patches": 6
                    },
                    "status_history": [
                        {
                            "evaluator": "",
                            "status": "Pass",
                            "timestamp": "2025-08-14T21:28:27.572760Z"
                        }
                    ],
                    "description": "Fail General Performance: When any metrics have value 0.",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Pass",
            "created": "2025-08-14T21:28:36.356426Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Processing",
            "name": "Licks",
            "description": "Licks",
            "metrics": [
                {
                    "name": "Inter-licks distribution",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "",
                            "status": "Pass",
                            "timestamp": "2025-08-14T21:28:27.572760Z"
                        }
                    ],
                    "description": "Fail when density < 0.1.",
                    "reference": "inter_licks_distribution.png",
                    "evaluated_assets": null
                },
                {
                    "name": "Number of licks",
                    "value": {
                        "Number of licks": 853
                    },
                    "status_history": [
                        {
                            "evaluator": "",
                            "status": "Pass",
                            "timestamp": "2025-08-14T21:28:27.572760Z"
                        }
                    ],
                    "description": "Fail when number of licks is 0 or above 1000.0.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "Within lick variability (onset - offset)",
                    "value": {
                        "Within lick variability (onset - offset)": 18.905045224087008
                    },
                    "status_history": [
                        {
                            "evaluator": "",
                            "status": "Pending",
                            "timestamp": "2025-08-14T21:28:27.572048Z"
                        }
                    ],
                    "description": "Within lick variability",
                    "reference": "licks.png",
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Pending",
            "created": "2025-08-14T21:28:36.356441Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Raw data",
            "name": "Data contract::ContractTestSuite",
            "description": null,
            "metrics": [
                {
                    "name": "ContractTestSuite::test_has_errors_on_load",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Fail",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if any non-excluded data streams had loading errors. // Message: The following DataStreams raised errors on load: \n VrForagingDataset::Behavior::HarpManipulator::Reserved8\nVrForagingDataset::Behavior::HarpManipulator::Reserved9\nVrForagingDataset::Behavior::HarpManipulator::Reserved10\nVrForagingDataset::Behavior::HarpManipulator::Reserved11\nVrForagingDataset::Behavior::HarpManipulator::Reserved12\nVrForagingDataset::Behavior::HarpManipulator::Reserved13\nVrForagingDataset::Behavior::HarpManipulator::Reserved14\nVrForagingDataset::Behavior::HarpManipulator::Reserved15\nVrForagingDataset::Behavior::SoftwareEvents::WaitLickOutcome\nVrForagingDataset::Behavior::SoftwareEvents::UpdaterStopDurationOffset\nVrForagingDataset::Behavior::SoftwareEvents::UpdaterStopVelocityThreshold\nVrForagingDataset::Behavior::SoftwareEvents::HabituationRewardAvailable\nVrForagingDataset::Behavior::Logs::Launcher\nVrForagingDataset::Behavior::Logs::EndSession",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "ContractTestSuite::test_has_excluded_as_warnings",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pending",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if any excluded data streams had loading errors and report as warnings. // Message: Found 387 DataStreams that raised ignored errors on load.",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Fail",
            "created": "2025-08-09T00:06:06.865645Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Raw data",
            "name": "HarpBehavior::HarpDeviceTestSuite",
            "description": null,
            "metrics": [
                {
                    "name": "HarpDeviceTestSuite::test_core_version",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the core version of the device matches the one provided // Message: Core version not specified, skipping test.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_fw_version_matches_reader",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the firmware version of the device matches the one in the reader // Message: Expected version 3.2.0 matches the device's version 3.2.0",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_has_whoami",
                    "value": 1216,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the harp board data stream is present and return its value // Message: None",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_match_whoami_to_yml",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the WhoAmI value matches the device's WhoAmI // Message: WhoAmI value matches the device's WhoAmI",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_read_dump_is_complete",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the read dump from an harp device is complete\n         // Message: Read dump is complete",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_registers_are_monotonicity",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check that the all the harp device registers' timestamps are monotonic\n         // Message: Monotonicity check passed. All registers are monotonic.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_request_response",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check that each request to the device has a corresponding response // Message: Request/Response check passed. All requests have a corresponding response.",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Pass",
            "created": "2025-08-09T00:06:06.865645Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Raw data",
            "name": "HarpManipulator::HarpDeviceTestSuite",
            "description": null,
            "metrics": [
                {
                    "name": "HarpDeviceTestSuite::test_core_version",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the core version of the device matches the one provided // Message: Core version not specified, skipping test.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_fw_version_matches_reader",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the firmware version of the device matches the one in the reader // Message: Expected version 0.7.0 matches the device's version 0.7.0",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_has_whoami",
                    "value": 1130,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the harp board data stream is present and return its value // Message: None",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_match_whoami_to_yml",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the WhoAmI value matches the device's WhoAmI // Message: WhoAmI value matches the device's WhoAmI",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_read_dump_is_complete",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Fail",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the read dump from an harp device is complete\n         // Message: Error during test execution: Harp register: <Reserved8> does not have loaded data",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_registers_are_monotonicity",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Fail",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check that the all the harp device registers' timestamps are monotonic\n         // Message: Error during test execution: Data has not been loaded yet.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_request_response",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check that each request to the device has a corresponding response // Message: Request/Response check passed. All requests have a corresponding response.",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Fail",
            "created": "2025-08-09T00:06:06.865645Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Raw data",
            "name": "HarpTreadmill::HarpDeviceTestSuite",
            "description": null,
            "metrics": [
                {
                    "name": "HarpDeviceTestSuite::test_core_version",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the core version of the device matches the one provided // Message: Core version not specified, skipping test.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_fw_version_matches_reader",
                    "value": false,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pending",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the firmware version of the device matches the one in the reader // Message: Expected version 0.0.0 is less than the device's version 0.1.0. Consider updating interface package.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_has_whoami",
                    "value": 1402,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the harp board data stream is present and return its value // Message: None",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_match_whoami_to_yml",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the WhoAmI value matches the device's WhoAmI // Message: WhoAmI value matches the device's WhoAmI",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_read_dump_is_complete",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the read dump from an harp device is complete\n         // Message: Read dump is complete",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_registers_are_monotonicity",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check that the all the harp device registers' timestamps are monotonic\n         // Message: Monotonicity check passed. All registers are monotonic.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_request_response",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check that each request to the device has a corresponding response // Message: Request/Response check passed. All requests have a corresponding response.",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Pending",
            "created": "2025-08-09T00:06:06.865645Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Raw data",
            "name": "HarpOlfactometer::HarpDeviceTestSuite",
            "description": null,
            "metrics": [
                {
                    "name": "HarpDeviceTestSuite::test_core_version",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the core version of the device matches the one provided // Message: Core version not specified, skipping test.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_fw_version_matches_reader",
                    "value": false,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Fail",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the firmware version of the device matches the one in the reader // Message: Expected version 1.3.0 is greater than the device's version 1.1.0. Consider updating the device firmware.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_has_whoami",
                    "value": 1140,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the harp board data stream is present and return its value // Message: None",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_match_whoami_to_yml",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the WhoAmI value matches the device's WhoAmI // Message: WhoAmI value matches the device's WhoAmI",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_read_dump_is_complete",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the read dump from an harp device is complete\n         // Message: Read dump is complete",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_registers_are_monotonicity",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check that the all the harp device registers' timestamps are monotonic\n         // Message: Monotonicity check passed. All registers are monotonic.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_request_response",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check that each request to the device has a corresponding response // Message: Request/Response check passed. All requests have a corresponding response.",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Fail",
            "created": "2025-08-09T00:06:06.865645Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Raw data",
            "name": "HarpSniffDetector::HarpDeviceTestSuite",
            "description": null,
            "metrics": [
                {
                    "name": "HarpDeviceTestSuite::test_core_version",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the core version of the device matches the one provided // Message: Core version not specified, skipping test.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_fw_version_matches_reader",
                    "value": false,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Fail",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the firmware version of the device matches the one in the reader // Message: Expected version 0.1.0 is greater than the device's version 0.0.0. Consider updating the device firmware.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_has_whoami",
                    "value": 1401,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the harp board data stream is present and return its value // Message: None",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_match_whoami_to_yml",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the WhoAmI value matches the device's WhoAmI // Message: WhoAmI value matches the device's WhoAmI",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_read_dump_is_complete",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the read dump from an harp device is complete\n         // Message: Read dump is complete",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_registers_are_monotonicity",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check that the all the harp device registers' timestamps are monotonic\n         // Message: Monotonicity check passed. All registers are monotonic.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_request_response",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check that each request to the device has a corresponding response // Message: Request/Response check passed. All requests have a corresponding response.",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Fail",
            "created": "2025-08-09T00:06:06.865645Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Raw data",
            "name": "HarpSniffDetector::HarpSniffDetectorTestSuite",
            "description": null,
            "metrics": [
                {
                    "name": "HarpSniffDetectorTestSuite::test_sniff_detector_physiology",
                    "value": {
                        "num_peaks": 16750,
                        "mean_ipi": 0.2394029494298167,
                        "std_ipi": 0.10822704674452456,
                        "breathing_rate_hz": 4.177057978532381,
                        "perc99": 10.869565217391305,
                        "perc01": 25.0
                    },
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Tests if the sniff detector is actually detecting sniffs by analyzing peaks in the signal. // Message: Breathing rate is 4.177057978532381 Hz",
                    "reference": "HarpSniffDetectorTestSuite_test_sniff_detector_physiology_cfc4621ddc6f46ebbbf0b212b4af9245.png",
                    "evaluated_assets": null
                },
                {
                    "name": "HarpSniffDetectorTestSuite::test_sniff_detector_sampling_rate",
                    "value": 249.9994653255248,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Tests if the sampling rate of the sniff detector is within nominal values // Message: Sampling rate is 250.00 Hz. Expected 250 Hz",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpSniffDetectorTestSuite::test_sniff_detector_signal_quality",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Tests the quality of the sniff detector signal by analyzing quantization, clustering, clipping, and sudden jumps. // Message: Signal quality is good",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpSniffDetectorTestSuite::test_whoami",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the WhoAmI value is correct // Message: WhoAmI value is 1401 as expected",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Pass",
            "created": "2025-08-09T00:06:06.865645Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Raw data",
            "name": "HarpLickometer::HarpDeviceTestSuite",
            "description": null,
            "metrics": [
                {
                    "name": "HarpDeviceTestSuite::test_core_version",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the core version of the device matches the one provided // Message: Core version not specified, skipping test.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_fw_version_matches_reader",
                    "value": false,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pending",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the firmware version of the device matches the one in the reader // Message: Expected version 0.0.0 is less than the device's version 0.9.0. Consider updating interface package.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_has_whoami",
                    "value": 1400,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the harp board data stream is present and return its value // Message: None",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_match_whoami_to_yml",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the WhoAmI value matches the device's WhoAmI // Message: WhoAmI value matches the device's WhoAmI",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_read_dump_is_complete",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the read dump from an harp device is complete\n         // Message: Read dump is complete",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_registers_are_monotonicity",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check that the all the harp device registers' timestamps are monotonic\n         // Message: Monotonicity check passed. All registers are monotonic.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_request_response",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Fail",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check that each request to the device has a corresponding response // Message: Request/Response check failed. Some requests do not have a corresponding response.",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Fail",
            "created": "2025-08-09T00:06:06.865645Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Raw data",
            "name": "HarpClockGenerator::HarpDeviceTestSuite",
            "description": null,
            "metrics": [
                {
                    "name": "HarpDeviceTestSuite::test_core_version",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the core version of the device matches the one provided // Message: Core version not specified, skipping test.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_fw_version_matches_reader",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the firmware version of the device matches the one in the reader // Message: Expected version 0.1.0 matches the device's version 0.1.0",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_has_whoami",
                    "value": 1404,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the harp board data stream is present and return its value // Message: None",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_match_whoami_to_yml",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the WhoAmI value matches the device's WhoAmI // Message: WhoAmI value matches the device's WhoAmI",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_read_dump_is_complete",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the read dump from an harp device is complete\n         // Message: Read dump is complete",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_registers_are_monotonicity",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check that the all the harp device registers' timestamps are monotonic\n         // Message: Monotonicity check passed. All registers are monotonic.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_request_response",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check that each request to the device has a corresponding response // Message: Request/Response check passed. All requests have a corresponding response.",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Pass",
            "created": "2025-08-09T00:06:06.865645Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Raw data",
            "name": "HarpEnvironmentSensor::HarpDeviceTestSuite",
            "description": null,
            "metrics": [
                {
                    "name": "HarpDeviceTestSuite::test_core_version",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the core version of the device matches the one provided // Message: Core version not specified, skipping test.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_fw_version_matches_reader",
                    "value": false,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pending",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the firmware version of the device matches the one in the reader // Message: Expected version 0.1.0 is less than the device's version 0.2.0. Consider updating interface package.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_has_whoami",
                    "value": 1405,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the harp board data stream is present and return its value // Message: None",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_match_whoami_to_yml",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the WhoAmI value matches the device's WhoAmI // Message: WhoAmI value matches the device's WhoAmI",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_read_dump_is_complete",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the read dump from an harp device is complete\n         // Message: Read dump is complete",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_registers_are_monotonicity",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check that the all the harp device registers' timestamps are monotonic\n         // Message: Monotonicity check passed. All registers are monotonic.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpDeviceTestSuite::test_request_response",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check that each request to the device has a corresponding response // Message: Request/Response check passed. All requests have a corresponding response.",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Pending",
            "created": "2025-08-09T00:06:06.865645Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Raw data",
            "name": "HarpHub::HarpHubTestSuite",
            "description": null,
            "metrics": [
                {
                    "name": "HarpHubTestSuite::test_clock_generator_reg",
                    "value": false,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Fail",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Checks if the clock generator device is actually a clock generator // Message: Clock generator is not a clock generator",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpHubTestSuite::test_devices_are_subordinate",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Checks if the devices are subordinate to the clock generator // Message: Device HarpBehavior is subordinate to the clock generator",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpHubTestSuite::test_devices_are_subordinate",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Checks if the devices are subordinate to the clock generator // Message: Device HarpManipulator is subordinate to the clock generator",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpHubTestSuite::test_devices_are_subordinate",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Checks if the devices are subordinate to the clock generator // Message: Device HarpTreadmill is subordinate to the clock generator",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpHubTestSuite::test_devices_are_subordinate",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Checks if the devices are subordinate to the clock generator // Message: Device HarpOlfactometer is subordinate to the clock generator",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpHubTestSuite::test_devices_are_subordinate",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Checks if the devices are subordinate to the clock generator // Message: Device HarpSniffDetector is subordinate to the clock generator",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpHubTestSuite::test_devices_are_subordinate",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Checks if the devices are subordinate to the clock generator // Message: Device HarpLickometer is subordinate to the clock generator",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpHubTestSuite::test_devices_are_subordinate",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Checks if the devices are subordinate to the clock generator // Message: Device HarpEnvironmentSensor is subordinate to the clock generator",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpHubTestSuite::test_is_read_dump_synchronized",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the read dump from the devices arrives are roughly the same time // Message: Device HarpBehavior read dump is synchronized with the clock generator's",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpHubTestSuite::test_is_read_dump_synchronized",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the read dump from the devices arrives are roughly the same time // Message: Device HarpManipulator read dump is synchronized with the clock generator's",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpHubTestSuite::test_is_read_dump_synchronized",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the read dump from the devices arrives are roughly the same time // Message: Device HarpTreadmill read dump is synchronized with the clock generator's",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpHubTestSuite::test_is_read_dump_synchronized",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the read dump from the devices arrives are roughly the same time // Message: Device HarpOlfactometer read dump is synchronized with the clock generator's",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpHubTestSuite::test_is_read_dump_synchronized",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the read dump from the devices arrives are roughly the same time // Message: Device HarpSniffDetector read dump is synchronized with the clock generator's",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpHubTestSuite::test_is_read_dump_synchronized",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the read dump from the devices arrives are roughly the same time // Message: Device HarpLickometer read dump is synchronized with the clock generator's",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "HarpHubTestSuite::test_is_read_dump_synchronized",
                    "value": true,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check if the read dump from the devices arrives are roughly the same time // Message: Device HarpEnvironmentSensor read dump is synchronized with the clock generator's",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Fail",
            "created": "2025-08-09T00:06:06.865645Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Raw data",
            "name": "FrontCamera::CameraTestSuite",
            "description": null,
            "metrics": [
                {
                    "name": "CameraTestSuite::test_check_dropped_frames",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if there are dropped frames in the metadata DataFrame.\n         // Message: No dropped frames detected in metadata.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CameraTestSuite::test_histogram_and_create_asset",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Checks the histogram of the video and ensures color is well distributed.\n        It also saves an asset with a single frame of the video and color histogram. // Message: Histogram and asset created successfully.",
                    "reference": "CameraTestSuite_test_histogram_and_create_asset_039704e2d87a462c84eb52b1cf657ace.png",
                    "evaluated_assets": null
                },
                {
                    "name": "CameraTestSuite::test_is_start_bounded",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the start time of the video is bounded by the provided start time. // Message: No start time provided, skipping test.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CameraTestSuite::test_is_stop_bounded",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the stop time of the video is bounded by the provided stop time. // Message: No stop time provided, skipping test.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CameraTestSuite::test_match_expected_fps",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the frames per second (FPS) of the video metadata matches the expected FPS. // Message: Mean frame period (-4.3262073611428226e-08) is within expected range: 0.002777777777777778",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CameraTestSuite::test_metadata_shape",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Checks if the metadata DataFrame has the expected shape. Including headers.\n         // Message: Metadata DataFrame has expected shape and columns",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CameraTestSuite::test_video_frame_count",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the number of frames in the video matches the number of rows in the metadata DataFrame.\n         // Message: Number of frames in video (1442188) matches number of rows in metadata (1442188)",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Pass",
            "created": "2025-08-09T00:06:06.865645Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Raw data",
            "name": "SideCamera::CameraTestSuite",
            "description": null,
            "metrics": [
                {
                    "name": "CameraTestSuite::test_check_dropped_frames",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if there are dropped frames in the metadata DataFrame.\n         // Message: No dropped frames detected in metadata.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CameraTestSuite::test_histogram_and_create_asset",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Checks the histogram of the video and ensures color is well distributed.\n        It also saves an asset with a single frame of the video and color histogram. // Message: Histogram and asset created successfully.",
                    "reference": "CameraTestSuite_test_histogram_and_create_asset_b0a6ca4988154b85ba05ee9f2c07f773.png",
                    "evaluated_assets": null
                },
                {
                    "name": "CameraTestSuite::test_is_start_bounded",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the start time of the video is bounded by the provided start time. // Message: No start time provided, skipping test.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CameraTestSuite::test_is_stop_bounded",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the stop time of the video is bounded by the provided stop time. // Message: No stop time provided, skipping test.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CameraTestSuite::test_match_expected_fps",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the frames per second (FPS) of the video metadata matches the expected FPS. // Message: Mean frame period (-4.3262073611428226e-08) is within expected range: 0.002777777777777778",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CameraTestSuite::test_metadata_shape",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Checks if the metadata DataFrame has the expected shape. Including headers.\n         // Message: Metadata DataFrame has expected shape and columns",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CameraTestSuite::test_video_frame_count",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the number of frames in the video matches the number of rows in the metadata DataFrame.\n         // Message: Number of frames in video (1442188) matches number of rows in metadata (1442188)",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Pass",
            "created": "2025-08-09T00:06:06.865645Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Raw data",
            "name": "FaceCamera::CameraTestSuite",
            "description": null,
            "metrics": [
                {
                    "name": "CameraTestSuite::test_check_dropped_frames",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if there are dropped frames in the metadata DataFrame.\n         // Message: No dropped frames detected in metadata.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CameraTestSuite::test_histogram_and_create_asset",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Checks the histogram of the video and ensures color is well distributed.\n        It also saves an asset with a single frame of the video and color histogram. // Message: Histogram and asset created successfully.",
                    "reference": "CameraTestSuite_test_histogram_and_create_asset_7ecd816caf1748d780db3601bcc4a523.png",
                    "evaluated_assets": null
                },
                {
                    "name": "CameraTestSuite::test_is_start_bounded",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the start time of the video is bounded by the provided start time. // Message: No start time provided, skipping test.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CameraTestSuite::test_is_stop_bounded",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the stop time of the video is bounded by the provided stop time. // Message: No stop time provided, skipping test.",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CameraTestSuite::test_match_expected_fps",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the frames per second (FPS) of the video metadata matches the expected FPS. // Message: Mean frame period (-4.3262073611428226e-08) is within expected range: 0.002777777777777778",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CameraTestSuite::test_metadata_shape",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Checks if the metadata DataFrame has the expected shape. Including headers.\n         // Message: Metadata DataFrame has expected shape and columns",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CameraTestSuite::test_video_frame_count",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the number of frames in the video matches the number of rows in the metadata DataFrame.\n         // Message: Number of frames in video (1442188) matches number of rows in metadata (1442188)",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Pass",
            "created": "2025-08-09T00:06:06.865645Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Raw data",
            "name": "CurrentPosition::CsvTestSuite",
            "description": null,
            "metrics": [
                {
                    "name": "CsvTestSuite::test_infer_missing_headers",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Infer if the DataFrame was loaded from a CSV without headers.\n         // Message: DataFramed was likely loaded from a CSV with headers",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CsvTestSuite::test_is_instance_of_pandas_dataframe",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the data stream is a pandas DataFrame.\n         // Message: Data stream is a pandas DataFrame",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CsvTestSuite::test_is_not_empty",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the DataFrame is not empty.\n         // Message: Data stream is not empty",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Pass",
            "created": "2025-08-09T00:06:06.865645Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Raw data",
            "name": "IsStopped::CsvTestSuite",
            "description": null,
            "metrics": [
                {
                    "name": "CsvTestSuite::test_infer_missing_headers",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Infer if the DataFrame was loaded from a CSV without headers.\n         // Message: DataFramed was likely loaded from a CSV with headers",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CsvTestSuite::test_is_instance_of_pandas_dataframe",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the data stream is a pandas DataFrame.\n         // Message: Data stream is a pandas DataFrame",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CsvTestSuite::test_is_not_empty",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the DataFrame is not empty.\n         // Message: Data stream is not empty",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Pass",
            "created": "2025-08-09T00:06:06.865645Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Raw data",
            "name": "Torque::CsvTestSuite",
            "description": null,
            "metrics": [
                {
                    "name": "CsvTestSuite::test_infer_missing_headers",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Infer if the DataFrame was loaded from a CSV without headers.\n         // Message: DataFramed was likely loaded from a CSV with headers",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CsvTestSuite::test_is_instance_of_pandas_dataframe",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the data stream is a pandas DataFrame.\n         // Message: Data stream is a pandas DataFrame",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CsvTestSuite::test_is_not_empty",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the DataFrame is not empty.\n         // Message: Data stream is not empty",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Pass",
            "created": "2025-08-09T00:06:06.865645Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Raw data",
            "name": "RendererSynchState::CsvTestSuite",
            "description": null,
            "metrics": [
                {
                    "name": "CsvTestSuite::test_infer_missing_headers",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Infer if the DataFrame was loaded from a CSV without headers.\n         // Message: DataFramed was likely loaded from a CSV with headers",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CsvTestSuite::test_is_instance_of_pandas_dataframe",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the data stream is a pandas DataFrame.\n         // Message: Data stream is a pandas DataFrame",
                    "reference": null,
                    "evaluated_assets": null
                },
                {
                    "name": "CsvTestSuite::test_is_not_empty",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Pass",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: \n        Check if the DataFrame is not empty.\n         // Message: Data stream is not empty",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Pass",
            "created": "2025-08-09T00:06:06.865645Z"
        },
        {
            "modality": {
                "name": "Behavior",
                "abbreviation": "behavior"
            },
            "stage": "Raw data",
            "name": "VrForaging::VrForagingQcSuite",
            "description": null,
            "metrics": [
                {
                    "name": "VrForagingQcSuite::test_end_session_exists",
                    "value": null,
                    "status_history": [
                        {
                            "evaluator": "Automated",
                            "status": "Fail",
                            "timestamp": "2025-08-09T00:06:06.865645Z"
                        }
                    ],
                    "description": "Test: Check that the session has an end event. // Message: EndSession event does not exist. Session may be corrupted or not ended properly.",
                    "reference": null,
                    "evaluated_assets": null
                }
            ],
            "tags": null,
            "notes": null,
            "allow_failed_metrics": false,
            "latest_status": "Fail",
            "created": "2025-08-09T00:06:06.865645Z"
        }
    ],
    "notes": null
}
```
