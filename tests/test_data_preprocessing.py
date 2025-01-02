
import unittest
from data_preprocessing import preprocess_data
import pandas as pd

class TestDataPreprocessing(unittest.TestCase):
    def test_preprocess_data(self):
        # Create mock dataset
        data = {
            'feature1': [1, 2, None],
            'feature2': ['A', 'B', 'C']
        }
        df = pd.DataFrame(data)
        df.to_csv('test_data.csv', index=False)

        # Preprocess data
        processed_data = preprocess_data('test_data.csv')

        # Test the output
        self.assertEqual(processed_data.shape[0], 3)  # Check row count
        self.assertTrue(processed_data.isna().sum().sum() == 0)  # Check no missing values

if __name__ == '__main__':
    unittest.main()
