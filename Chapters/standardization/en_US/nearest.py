import numpy as np
from penguins import load_penguins

data = load_penguins()
names = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
X = np.column_stack([data[name] for name in names])   # 333 rows, 4 columns
species = data["species"]

def nearest(features, i):
    """Row number of the penguin closest to penguin i."""
    distances = np.sqrt(np.sum((features - features[i])**2, axis=1))
    distances[i] = np.inf          # do not count the penguin itself
    return np.argmin(distances)

mystery = 91
print("Mystery penguin:", species[mystery], X[mystery])

j = nearest(X, mystery)
print("Nearest in raw units:", species[j], X[j])

Z = (X - X.mean(axis=0)) / X.std(axis=0)   # standardize every column
j = nearest(Z, mystery)
print("Nearest after standardizing:", species[j], X[j])
