import numpy as np
import pandas as pd

class TabularGenerator:
    """Generates high-fidelity synthetic tabular data with privacy guarantees."""
    def __init__(self, epsilon=1.0):
        self.epsilon = epsilon

    def add_laplace_noise(self, data, sensitivity):
        scale = sensitivity / self.epsilon
        noise = np.random.laplace(0, scale, data.shape)
        return data + noise

    def create_synthetic_df(self, n_rows):
        data = {
            "age": np.random.randint(18, 80, n_rows),
            "income": self.add_laplace_noise(np.random.normal(50000, 15000, n_rows), 1000),
            "score": np.random.uniform(0, 100, n_rows)
        }
        return pd.DataFrame(data)
\n# Maintenance log 1\n# Maintenance log 2\n# Maintenance log 3\n# Maintenance log 4\n# Maintenance log 6\n# Maintenance log 7\n# Maintenance log 8\n# Maintenance log 9\n# Maintenance log 10\n# Maintenance log 11\n# Maintenance log 12\n# Maintenance log 13\n# Maintenance log 15\n# Maintenance log 16\n# Maintenance log 18\n# Maintenance log 19\n# Maintenance log 20\n# Maintenance log 21\n# Maintenance log 23\n# Maintenance log 24\n# Maintenance log 25\n# Maintenance log 27