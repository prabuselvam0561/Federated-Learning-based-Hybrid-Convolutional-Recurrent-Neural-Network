import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv1D, LSTM, Flatten
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split

def build_model(input_shape):
    model = Sequential([
        Conv1D(filters=32, kernel_size=3, activation='relu', input_shape=input_shape),
        Conv1D(filters=64, kernel_size=3, activation='relu'),
        Flatten(),
        LSTM(128, return_sequences=True),
        LSTM(64),
        Dense(128, activation='relu'),
        Dense(64, activation='relu'),
        Dense(10, activation='softmax')  # Adjust the number of classes as required
    ])
    
    model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model(data, labels):
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    input_shape = (X_train.shape[1], X_train.shape[2])
    model = build_model(input_shape)
    
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=32)
    return model

if __name__ == '__main__':
    # Example usage
    import numpy as np
    
    # Mock data for demonstration
    data = np.random.rand(1000, 50, 1)  # Replace with actual data
    labels = tf.keras.utils.to_categorical(np.random.randint(0, 10, size=(1000,)), num_classes=10)
    
    trained_model = train_model(data, labels)
    print("Model training complete.")
