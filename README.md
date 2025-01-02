# Federated Learning-based Hybrid Convolutional Recurrent Neural Network for Multi-Class Intrusion Detection in IoT Networks

## Overview

This repository contains the implementation of the hybrid Convolutional Recurrent Neural Network (CRNN) integrated with federated learning, developed for multi-class intrusion detection in Internet of Things (IoT) networks. This project aligns with the research paper titled "Federated Learning-based Hybrid Convolutional Recurrent Neural Network for Multi-Class Intrusion Detection in IoT Networks."

The hybrid CRNN combines spatial and temporal feature learning using Convolutional Neural Networks (CNN) and Long Short-Term Memory (LSTM) layers. It is designed for privacy-preserving and scalable deployment in both centralized and federated environments, achieving robust performance across diverse attack types.

---

## Key Features

1. **Hybrid Model Architecture**:
   - Utilizes CNN for spatial feature extraction and LSTM for temporal pattern recognition.
   - Achieves high accuracy and precision across multiple attack classes.

2. **Federated Learning Integration**:
   - Ensures data privacy by enabling decentralized training.
   - Aggregates local models using federated averaging to form a global model.

3. **Performance Metrics**:
   - Accuracy: 94%
   - Balanced precision and recall for high- and low-prevalence attack types.

4. **Real-World Dataset**:
   - Evaluated using the Edge-IIoT dataset containing diverse IoT/IIoT attack scenarios.

---

## Repository Structure

```plaintext
Project-Name/
├── README.md                   # Project overview (this file)
├── LICENSE                     # Licensing information
├── requirements.txt            # Python dependencies
├── src/                        # Source code for the project
│   ├── data_preprocessing.py   # Data cleaning and normalization
│   ├── feature_engineering.py  # Feature extraction scripts
│   ├── model_training.py       # Model training scripts
│   ├── federated_learning.py   # Federated training implementation
│   ├── evaluation.py           # Evaluation and metrics scripts
│   └── utils/                  # Utility functions
│       ├── data_loader.py      # Data loading utilities
│       ├── model_utils.py      # Model-related utilities
│       └── metrics.py          # Metric calculation functions
├── notebooks/                  # Jupyter notebooks for demonstration
│   ├── Exploratory_Data_Analysis.ipynb
│   ├── Model_Training.ipynb
│   └── Evaluation_Results.ipynb
├── datasets/                   # Dataset and related information
│   ├── README.md
│   └── sample_data/
│       ├── training_set.csv
│       └── testing_set.csv
├── docs/                       # Documentation
│   ├── Installation_Guide.md
│   ├── User_Manual.md
│   ├── Replication_Guide.md
│   ├── Model_Architecture_Details.md
│   └── FAQ.md
├── tests/                      # Unit tests for project components
│   ├── test_data_preprocessing.py
│   ├── test_feature_engineering.py
│   ├── test_model_training.py
│   └── test_federated_learning.py
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.md
    │   └── feature_request.md
    ├── PULL_REQUEST_TEMPLATE.md
    └── workflows/
        └── python-app.yml
```

---

## Installation

### Prerequisites

- Python 3.8+
- Git
- Virtual environment (optional but recommended)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/project-name.git
   cd project-name
   ```

2. **Set up Virtual Environment** (optional):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Tests**:
   ```bash
   pytest tests/
   ```

---

## Usage

### Running the Model

1. **Preprocess the Data**:
   ```bash
   python src/data_preprocessing.py
   ```

2. **Train the Model**:
   - Centralized:
     ```bash
     python src/model_training.py
     ```
   - Federated:
     ```bash
     python src/federated_learning.py
     ```

3. **Evaluate the Model**:
   ```bash
   python src/evaluation.py
   ```

### Jupyter Notebooks

Use the notebooks in the `notebooks/` folder for detailed demonstrations of data analysis, training, and evaluation.

---

## Dataset

### Description
The Edge-IIoT dataset contains IoT/IIoT network traffic data with labeled attack types. It includes:
- **Normal traffic**
- **14 different cyber-attacks**, grouped into 5 major categories:
  - DoS/DDoS attacks
  - Information Gathering
  - MITM attacks
  - Injection attacks
  - Malware attacks

### Access
Sample datasets are provided in the `datasets/sample_data/` folder. For the complete dataset, please contact the corresponding author.

---

## Documentation

Detailed documentation is available in the `docs/` folder:

- **Installation_Guide.md**: Step-by-step setup instructions.
- **User_Manual.md**: How to use the repository components.
- **Replication_Guide.md**: Instructions for replicating the experiments.
- **Model_Architecture_Details.md**: In-depth explanation of the hybrid CRNN architecture.
- **FAQ.md**: Common issues and their resolutions.

---

## Acknowledgments

- Authors of the research paper.
- Community contributors.
- Research institutions supporting IoT cybersecurity.

---

## Contact

For any questions or issues, please contact:
- **Prabu Selvam** (prabuselvam0561@gmail.com)
- Or raise an issue in this repository.

