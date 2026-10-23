import numpy as np
from penguins import load_penguins

data = load_penguins()
flipper = data["flipper_length_mm"]
y = data["body_mass_g"]
n = len(y)

def descend(X, alpha, steps):
    theta = np.zeros(X.shape[1])
    for _ in range(steps):
        gradient = 2 / n * X.T @ (X @ theta - y)
        theta = theta - alpha * gradient
    rmse = np.sqrt(np.mean((X @ theta - y)**2))
    return theta, rmse

# Raw flipper lengths: anything much above 2e-5 blows up
X_raw = np.column_stack([np.ones(n), flipper])
for steps in [100, 10_000, 1_000_000]:
    theta, rmse = descend(X_raw, 2e-5, steps)
    print(f"raw, {steps:>9,} steps:", np.round(theta, 1) + 0.0, f"RMSE {rmse:.0f}")

# Standardized flipper lengths
mean, sd = np.mean(flipper), np.std(flipper)
X_std = np.column_stack([np.ones(n), (flipper - mean) / sd])
for steps in [10, 30, 100]:
    theta, rmse = descend(X_std, 0.1, steps)
    print(f"standardized, {steps:>3} steps:", np.round(theta, 1),
          f"RMSE {rmse:.0f}")

# Convert back to grams per millimeter
b1 = theta[1] / sd
b0 = theta[0] - b1 * mean
print(f"mass = {b0:.1f} + {b1:.2f} * flipper")
