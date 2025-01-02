from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import numpy as np

def evaluate_model(y_true, y_pred, labels):
    metrics = {
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, average='weighted', zero_division=0),
        'recall': recall_score(y_true, y_pred, average='weighted', zero_division=0),
        'f1_score': f1_score(y_true, y_pred, average='weighted', zero_division=0),
        'confusion_matrix': confusion_matrix(y_true, y_pred, labels=labels).tolist()
    }
    return metrics

if __name__ == '__main__':
    # Example usage
    y_true = np.random.randint(0, 5, 100)  # Replace with actual ground truth
    y_pred = np.random.randint(0, 5, 100)  # Replace with actual predictions
    labels = [0, 1, 2, 3, 4]  # Replace with actual class labels
    
    evaluation_results = evaluate_model(y_true, y_pred, labels)
    print("Evaluation Results:")
    for metric, value in evaluation_results.items():
        print(f"{metric}: {value}")

