
import pandas as pd

def load_data(file_path):
    """
    Loads the dataset from the specified file path.
    :param file_path: Path to the dataset file (CSV format).
    :return: Loaded dataset as a Pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
