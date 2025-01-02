import pandas as pd

def engineer_features(data):
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
