
import unittest
from federated_learning import FederatedLearning
import numpy as np
import tensorflow as tf

class TestFederatedLearning(unittest.TestCase):
    def test_federated_learning(self):
        # Initialize federated learning
        num_clients = 3
        input_shape = (50,)
        num_classes = 10

        federated = FederatedLearning(num_clients, input_shape, num_classes)

        # Create mock data
        client_data = [np.random.rand(20, 50) for _ in range(num_clients)]
        client_labels = [tf.keras.utils.to_categorical(np.random.randint(0, 10, 20), num_classes=num_classes) for _ in range(num_clients)]

        # Train clients
        federated.train_clients(client_data, client_labels)

        # Aggregate models
        federated.aggregate_models()

        # Test global model's structure
        self.assertEqual(len(federated.global_model.layers), 3)

if __name__ == '__main__':
    unittest.main()
