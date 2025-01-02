
import unittest
from feature_engineering import engineer_features
import pandas as pd

class TestFeatureEngineering(unittest.TestCase):
    def test_engineer_features(self):
        # Create mock dataset
        data = {
            'protocol_type': ['TCP', 'UDP', 'HTTP'],
            'packet_count': [10, 20, 30],
            'duration': [1, 2, 0.5],
            'latency': [0.2, 0.3, 0.1]
        }
        df = pd.DataFrame(data)

        # Engineer features
        engineered_data = engineer_features(df)

        # Test the output
        self.assertIn('packet_frequency', engineered_data.columns)
        self.assertIn('protocol_consistency', engineered_data.columns)

if __name__ == '__main__':
    unittest.main()
