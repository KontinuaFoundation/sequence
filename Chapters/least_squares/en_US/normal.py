import numpy as np
from penguins import load_penguins

data = load_penguins()
x = data["flipper_length_mm"]
y = data["body_mass_g"]

# Design matrix: a column of ones, then the flipper lengths
X = np.column_stack([np.ones(len(x)), x])
print("X has shape", X.shape)

# Solve the normal equations
b = np.linalg.solve(X.T @ X, X.T @ y)
print("Normal equations:", np.round(b, 2))

# Let NumPy do the whole least squares problem
b, *_ = np.linalg.lstsq(X, y)
print("lstsq:           ", np.round(b, 2))

# Residuals are perpendicular to every column of X
residuals = y - X @ b
print("X^T e =", np.round(X.T @ residuals, 6) + 0.0)
