import numpy as np
from penguins import load_penguins

data = load_penguins()
x = data["flipper_length_mm"]
y = data["body_mass_g"]

rng = np.random.default_rng(seed=4)
order = rng.permutation(len(x))
train, val = order[:12], order[12:62]     # only 12 penguins to learn from

# Rescale x so that high powers of it stay reasonable
mean, sd = x[train].mean(), x[train].std()
z = (x - mean) / sd

def rmse(actual, predicted):
    return np.sqrt(np.mean((actual - predicted)**2))

print("degree  train RMSE  val RMSE")
for degree in range(1, 9):
    coefficients = np.polyfit(z[train], y[train], degree)
    train_error = rmse(y[train], np.polyval(coefficients, z[train]))
    val_error = rmse(y[val], np.polyval(coefficients, z[val]))
    print(f"{degree:6d} {train_error:11.0f} {val_error:9.0f}")
