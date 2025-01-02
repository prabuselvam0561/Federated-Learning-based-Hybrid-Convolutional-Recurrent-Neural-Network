
# Dataset Description

## Overview
The dataset used in this project is designed for IoT and IIoT intrusion detection. It contains a variety of network traffic data, labeled according to the type of activity (normal or specific attack types).

## Structure
- **`training_set.csv`**: The training dataset used for building the model.
- **`testing_set.csv`**: The testing dataset used for evaluating the model.

## Features
1. **Numerical Features**: 
   - Packet count
   - Duration
   - Latency
2. **Categorical Features**: 
   - Protocol type
   - Attack label (target)

## Attack Types
The dataset includes the following types of attacks:
- DDoS (HTTP, TCP, UDP, ICMP)
- SQL Injection
- Man-in-the-Middle (MITM)
- Port Scanning
- Ransomware
- Others

## Usage
- Place the `training_set.csv` and `testing_set.csv` files in the `sample_data` directory.
- Update the paths in the code scripts as needed to point to these files.

## License
Ensure you comply with the dataset license if sourced externally.
