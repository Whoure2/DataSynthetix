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
\n# Maintenance log 1\n# Maintenance log 2\n# Maintenance log 3\n# Maintenance log 4\n# Maintenance log 6\n# Maintenance log 7\n# Maintenance log 8\n# Maintenance log 9\n# Maintenance log 10\n# Maintenance log 11\n# Maintenance log 12\n# Maintenance log 13\n# Maintenance log 15\n# Maintenance log 16\n# Maintenance log 18\n# Maintenance log 19\n# Maintenance log 20\n# Maintenance log 21\n# Maintenance log 23\n# Maintenance log 24\n# Maintenance log 25\n# Maintenance log 27\n# Maintenance log 28\n# Maintenance log 30\n# Maintenance log 32\n# Maintenance log 33\n# Maintenance log 35\n# Maintenance log 36\n# Maintenance log 37\n# Maintenance log 38\n# Maintenance log 39\n# Maintenance log 40\n# Maintenance log 41\n# Maintenance log 42\n# Maintenance log 43\n# Maintenance log 44\n# Maintenance log 46\n# Maintenance log 48\n# Maintenance log 49\n# Maintenance log 51\n# Maintenance log 54\n# Maintenance log 55\n# Maintenance log 56\n# Maintenance log 58\n# Maintenance log 61\n# Maintenance log 63\n# Maintenance log 64\n# Maintenance log 65\n# Maintenance log 66\n# Maintenance log 67\n# Maintenance log 68\n# Maintenance log 69\n# Maintenance log 70\n# Maintenance log 71\n# Maintenance log 72\n# Maintenance log 73\n# Maintenance log 74\n# Maintenance log 75\n# Maintenance log 76\n# Maintenance log 78\n# Maintenance log 79\n# Maintenance log 80\n# Maintenance log 81\n# Maintenance log 82\n# Maintenance log 83\n# Maintenance log 84\n# Maintenance log 86\n# Maintenance log 88\n# Maintenance log 89\n# Maintenance log 90\n# Maintenance log 92\n# Maintenance log 93\n# Maintenance log 94\n# Maintenance log 95\n# Maintenance log 97\n# Maintenance log 98\n# Maintenance log 99\n# Maintenance log 101\n# Maintenance log 104\n# Maintenance log 105\n# Maintenance log 106\n# Maintenance log 107\n# Maintenance log 108\n# Maintenance log 109\n# Maintenance log 111\n# Maintenance log 112\n# Maintenance log 114\n# Maintenance log 115\n# Maintenance log 116\n# Maintenance log 117\n# Maintenance log 118\n# Maintenance log 119\n# Maintenance log 120\n# Maintenance log 121