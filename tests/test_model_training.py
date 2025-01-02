
import unittest
from model_training import train_model
import numpy as np
import tensorflow as tf

class TestModelTraining(unittest.TestCase):
    def test_train_model(self):
        # Create mock data
        data = np.random.rand(100, 50, 1)
        labels = tf.keras.utils.to_categorical(np.random.randint(0, 10, 100), num_classes=10)

        # Train the model
        model = train_model(data, labels)

        # Test the model's architecture
        self.assertEqual(len(model.layers), 6)  # Check number of layers

if __name__ == '__main__':
    unittest.main()
