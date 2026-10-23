import numpy as np
from penguins import load_penguins

data = load_penguins()
n = len(data["species"])

rng = np.random.default_rng(seed=1)    # a fixed seed makes the shuffle repeatable
order = rng.permutation(n)             # the numbers 0 to n-1, shuffled

n_train = int(0.70 * n)
n_val = int(0.15 * n)
train = order[:n_train]
val = order[n_train:n_train + n_val]
test = order[n_train + n_val:]
print("Sizes:", len(train), len(val), len(test))

for name, rows in [("train", train), ("val", val), ("test", test)]:
    kinds, counts = np.unique(data["species"][rows], return_counts=True)
    shares = ", ".join(f"{k} {c / len(rows):.0%}" for k, c in zip(kinds, counts))
    print(f"{name:5s} {shares}")
