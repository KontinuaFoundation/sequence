import numpy as np
from penguins import load_penguins

data = load_penguins()
y = data["body_mass_g"]
n = len(y)

columns = {
    "intercept": np.ones(n),
    "flipper": data["flipper_length_mm"],
    "male": (data["sex"] == "male").astype(float),
    "Chinstrap": (data["species"] == "Chinstrap").astype(float),
    "Gentoo": (data["species"] == "Gentoo").astype(float),
}

# The same split as the Preparing Data chapter
order = np.random.default_rng(1).permutation(n)
train, test = order[:250], order[250:]

def rmse(X, b, rows):
    return np.sqrt(np.mean((y[rows] - X[rows] @ b)**2))

models = [["intercept", "flipper"],
          ["intercept", "flipper", "male"],
          ["intercept", "flipper", "male", "Chinstrap", "Gentoo"]]
for names in models:
    X = np.column_stack([columns[c] for c in names])
    b, *_ = np.linalg.lstsq(X[train], y[train])
    print(f"{len(names) - 1} features: train RMSE {rmse(X, b, train):.0f}, "
          f"test RMSE {rmse(X, b, test):.0f}")

for name, coef in zip(names, b):
    print(f"  {name:10s} {coef:8.1f}")
