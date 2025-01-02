import tensorflow as tf
import numpy as np

class FederatedLearning:
    def __init__(self, num_clients, input_shape, num_classes):
        self.num_clients = num_clients
        self.global_model = self.build_model(input_shape, num_classes)
        self.client_models = [self.build_model(input_shape, num_classes) for _ in range(num_clients)]
    
    def build_model(self, input_shape, num_classes):
        model = tf.keras.Sequential([
            tf.keras.layers.Flatten(input_shape=input_shape),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(num_classes, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def train_clients(self, client_data, client_labels, epochs=1, batch_size=32):
        for i in range(self.num_clients):
            self.client_models[i].fit(client_data[i], client_labels[i], epochs=epochs, batch_size=batch_size, verbose=0)

    def aggregate_models(self):
        global_weights = self.global_model.get_weights()
        for layer_weights in range(len(global_weights)):
            global_weights[layer_weights] = np.mean(
                [client_model.get_weights()[layer_weights] for client_model in self.client_models], axis=0
            )
        self.global_model.set_weights(global_weights)

    def evaluate_global_model(self, data, labels):
        return self.global_model.evaluate(data, labels, verbose=0)

if __name__ == '__main__':
    # Example usage
    num_clients = 3
    input_shape = (50,)
    num_classes = 10
    
    # Mock data for demonstration
    client_data = [np.random.rand(200, 50) for _ in range(num_clients)]
    client_labels = [tf.keras.utils.to_categorical(np.random.randint(0, 10, 200), num_classes=num_classes) for _ in range(num_clients)]
    test_data = np.random.rand(200, 50)
    test_labels = tf.keras.utils.to_categorical(np.random.randint(0, 10, 200), num_classes=num_classes)
    
    # Federated learning process
    federated = FederatedLearning(num_clients, input_shape, num_classes)
    federated.train_clients(client_data, client_labels, epochs=5)
    federated.aggregate_models()
    metrics = federated.evaluate_global_model(test_data, test_labels)
    print(f"Global model evaluation: {metrics}")

