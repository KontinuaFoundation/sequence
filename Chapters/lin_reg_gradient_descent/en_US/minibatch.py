import numpy as np
from penguins import load_penguins

data = load_penguins()
flipper = data["flipper_length_mm"]
y = data["body_mass_g"]
n = len(y)
X = np.column_stack([np.ones(n), (flipper - np.mean(flipper)) / np.std(flipper)])

rng = np.random.default_rng(0)
theta = np.zeros(2)
alpha, batch_size = 0.1, 32
for epoch in range(1, 6):
    order = rng.permutation(n)                  # shuffle once per epoch
    for start in range(0, n, batch_size):
        rows = order[start:start + batch_size]
        Xb, yb = X[rows], y[rows]
        gradient = 2 / len(rows) * Xb.T @ (Xb @ theta - yb)
        theta = theta - alpha * gradient
    rmse = np.sqrt(np.mean((X @ theta - y)**2))
    print(f"epoch {epoch}: theta = {np.round(theta, 1)}, RMSE = {rmse:.1f}")
