
from sklearn.metrics import classification_report

def generate_classification_report(y_true, y_pred, labels):
    """
    Generates a classification report.
    :param y_true: Ground truth labels.
    :param y_pred: Predicted labels.
    :param labels: List of class labels.
    :return: Classification report as a string.
    """
    try:
        report = classification_report(y_true, y_pred, target_names=labels, zero_division=0)
        print("Classification Report Generated:")
        print(report)
        return report
    except Exception as e:
        print(f"Error generating classification report: {e}")
        return None
