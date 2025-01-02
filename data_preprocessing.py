data_preprocessing_content = """
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def preprocess_data(file_path):
    \"\"\"
    Preprocesses the IoT dataset by handling missing values, normalizing numerical features,
    and encoding categorical variables.
    :param file_path: Path to the dataset file (CSV format).
    :return: Processed dataset as a Pandas DataFrame.
    \"\"\"
    # Load dataset
    data = pd.read_csv(file_path)
    
    # Handle missing values
    data.fillna(method='ffill', inplace=True)
    
    # Normalize numerical features
    numerical_features = data.select_dtypes(include=['int64', 'float64']).columns
    scaler = StandardScaler()
    data[numerical_features] = scaler.fit_transform(data[numerical_features])
    
    # One-hot encode categorical features
    categorical_features = data.select_dtypes(include=['object']).columns
    encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
    encoded_data = pd.DataFrame(encoder.fit_transform(data[categorical_features]))
    encoded_data.columns = encoder.get_feature_names_out(categorical_features)
    
    # Combine numerical and encoded categorical features
    data = pd.concat([data[numerical_features], encoded_data], axis=1)
    
    return data

if __name__ == '__main__':
    # Example usage
    dataset_path = 'content/data/sample_data/training_set.csv'
    processed_data = preprocess_data(dataset_path)
    print(f"Processed data shape: {processed_data.shape}")
"""

# Save the content to a new path
file_path_updated = "content/data/data_preprocessing.py"

# Ensure the directory exists before saving
import os
os.makedirs("content/data", exist_ok=True)

with open(file_path_updated, "w") as file:
    file.write(data_preprocessing_content)

file_path_updated
