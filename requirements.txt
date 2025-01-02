# Requirements for Federated Learning-based Hybrid CRNN

Below is the list of Python dependencies required to run this project:

```
tensorflow==2.9.1
keras==2.9.0
numpy==1.21.6
pandas==1.3.5
scikit-learn==1.0.2
matplotlib==3.5.1
seaborn==0.11.2
jupyter==1.0.0
pytest==7.1.2
flask==2.1.2
```

---

## Installing Dependencies

1. **Using `pip`**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Using Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **For GPU Support (Optional)**:
   Ensure you have the appropriate GPU drivers and CUDA/cuDNN versions installed. Refer to TensorFlow's [GPU support guide](https://www.tensorflow.org/install/gpu).

---

## Updating Requirements

If additional dependencies are added, update the `requirements.txt` by freezing the environment:

```bash
pip freeze > requirements.txt
```

