
import tensorflow as tf

def save_model(model, file_path):
    """
    Saves the trained model to the specified file path.
    :param model: Trained model instance.
    :param file_path: Path to save the model.
    """
    try:
        model.save(file_path)
        print(f"Model saved successfully at {file_path}")
    except Exception as e:
        print(f"Error saving model: {e}")

def load_model(file_path):
    """
    Loads a model from the specified file path.
    :param file_path: Path to the saved model.
    :return: Loaded model instance.
    """
    try:
        model = tf.keras.models.load_model(file_path)
        print(f"Model loaded successfully from {file_path}")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None
