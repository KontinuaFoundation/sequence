import numpy as np
from penguins import load_penguins

data = load_penguins()
names, y = np.unique(data["species"], return_inverse=True)
features = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
X = np.column_stack([data[f] for f in features])
order = np.random.default_rng(1).permutation(len(y))
dev, test = order[:266], order[266:]

def gini(labels):
    p = np.bincount(labels, minlength=3) / len(labels)
    return 1 - np.sum(p**2)

def best_split(X, y):
    """Try every feature and every threshold; return the lowest weighted Gini."""
    best = (gini(y), None, None)                # (impurity, feature, threshold)
    for j in range(X.shape[1]):
        values = np.unique(X[:, j])
        for t in (values[:-1] + values[1:]) / 2:  # midpoints between values
            left = X[:, j] <= t
            g = (left.sum() * gini(y[left]) + (~left).sum() * gini(y[~left])) / len(y)
            if g < best[0]:
                best = (g, j, t)
    return best

def grow(X, y, depth, max_depth):
    majority = np.bincount(y, minlength=3).argmax()
    if depth == max_depth or gini(y) == 0:
        return {"leaf": majority, "counts": np.bincount(y, minlength=3)}
    g, j, t = best_split(X, y)
    if j is None:                               # no split helps
        return {"leaf": majority, "counts": np.bincount(y, minlength=3)}
    left = X[:, j] <= t
    return {"feature": j, "threshold": t,
            "left": grow(X[left], y[left], depth + 1, max_depth),
            "right": grow(X[~left], y[~left], depth + 1, max_depth)}

def predict_one(node, x):
    while "leaf" not in node:
        node = node["left"] if x[node["feature"]] <= node["threshold"] else node["right"]
    return node["leaf"]

def predict(tree, X):
    return np.array([predict_one(tree, x) for x in X])

def show(node, indent="", label=""):
    if "leaf" in node:
        print(f"{indent}{label}{names[node['leaf']]} {node['counts']}")
    else:
        print(f"{indent}{label}{features[node['feature']]} <= {node['threshold']:.2f}?")
        show(node["left"], indent + "    ", "yes: ")
        show(node["right"], indent + "    ", "no:  ")

tree = grow(X[dev], y[dev], 0, max_depth=2)
show(tree)
for depth in [1, 2, 3, 4, 6, 10]:
    tree = grow(X[dev], y[dev], 0, depth)
    train_acc = np.mean(predict(tree, X[dev]) == y[dev])
    test_acc = np.mean(predict(tree, X[test]) == y[test])
    print(f"max depth {depth:2d}: training {train_acc:.3f}, test {test_acc:.3f}")
