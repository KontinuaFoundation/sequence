import numpy as np
from penguins import load_penguins

data = load_penguins()
y = data["body_mass_g"]
n = len(y)
order = np.random.default_rng(1).permutation(n)
train, test = order[:250], order[250:]

# 40 columns of pure random numbers: no information about penguins
junk = np.random.default_rng(0).normal(size=(n, 40))

print("junk   R^2   adj R^2   test RMSE")
for k in [0, 5, 10, 20, 40]:
    X = np.column_stack([np.ones(n), data["flipper_length_mm"], junk[:, :k]])
    b, *_ = np.linalg.lstsq(X[train], y[train])
    res = y[train] - X[train] @ b
    r2 = 1 - np.sum(res**2) / np.sum((y[train] - np.mean(y[train]))**2)
    p = k + 1                              # number of features
    adj = 1 - (1 - r2) * (250 - 1) / (250 - p - 1)
    rmse = np.sqrt(np.mean((y[test] - X[test] @ b)**2))
    print(f"{k:4d}  {r2:.3f}   {adj:.3f}    {rmse:.0f}")
