import numpy as np
from penguins import load_penguins

data = load_penguins()
n = len(data["species"])
order = np.random.default_rng(seed=1).permutation(n)
train, test = order[:250], order[250:]

# 1. Numbers: standardize with the TRAINING mean and standard deviation
names = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
numbers = np.column_stack([data[name] for name in names])
mean = numbers[train].mean(axis=0)
sd = numbers[train].std(axis=0)
scaled = (numbers - mean) / sd

# 2. Categories: one-hot encode the island, dropping one column (Biscoe)
islands = np.array(["Dream", "Torgersen"])
island_columns = (data["island"][:, None] == islands[None, :]).astype(float)

# 3. Two categories need only one column
male = (data["sex"] == "male").astype(float)[:, None]

X = np.hstack([scaled, island_columns, male])
print("Feature matrix:", X.shape)
print("First penguin: ", np.round(X[0], 2))
# Adding 0.0 turns a printed -0.0 into 0.0
print("Training means:", np.round(X[train, :4].mean(axis=0), 2) + 0.0)
print("Test means:    ", np.round(X[test, :4].mean(axis=0), 2) + 0.0)
