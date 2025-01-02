feature_engineering_content = """
import pandas as pd

def engineer_features(data):
    \"\"\"
    Performs feature engineering on the processed dataset to create new composite features
    that enhance the model's ability to detect anomalies.
    :param data: Processed dataset as a Pandas DataFrame.
    :return: Dataset with engineered features as a Pandas DataFrame.
    \"\"\"
    # Add a feature for protocol consistency
    data['protocol_consistency'] = data['protocol_type'].apply(lambda x: 1 if x in ['TCP', 'UDP'] else 0)
    
    # Create a feature for data packet frequency
    data['packet_frequency'] = data['packet_count'] / data['duration']
    data['packet_frequency'].fillna(0, inplace=True)  # Handle division by zero
    
    # Add a feature for abnormal latency detection
    data['abnormal_latency'] = data['latency'].apply(lambda x: 1 if x > 1.5 else 0)
    
    return data

if __name__ == '__main__':
    # Example usage
    dataset_path = 'content/data/sample_data/training_set.csv'
    data = pd.read_csv(dataset_path)
    engineered_data = engineer_features(data)
    print(f"Engineered data shape: {engineered_data.shape}")
"""

# Save the content to a new file
feature_engineering_file_path = "/content/data/feature_engineering.py"

# Write to file
with open(feature_engineering_file_path, "w") as file:
    file.write(feature_engineering_content)

feature_engineering_file_path
