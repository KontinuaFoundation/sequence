"""Decision trees from the Decision Trees chapter, with one addition:
each split may consider only a random subset of the features."""
import numpy as np

def gini(labels):
    p = np.bincount(labels, minlength=3) / len(labels)
    return 1 - np.sum(p**2)

def best_split(X, y, columns):
    best = (gini(y), None, None)
    for j in columns:
        values = np.unique(X[:, j])
        for t in (values[:-1] + values[1:]) / 2:
            left = X[:, j] <= t
            g = (left.sum() * gini(y[left]) + (~left).sum() * gini(y[~left])) / len(y)
            if g < best[0]:
                best = (g, j, t)
    return best

def grow(X, y, max_depth=None, max_features=None, rng=None, depth=0):
    majority = np.bincount(y, minlength=3).argmax()
    if depth == max_depth or gini(y) == 0:
        return {"leaf": majority}
    columns = range(X.shape[1])
    if max_features is not None:                 # random forest: a random subset
        columns = rng.choice(X.shape[1], size=max_features, replace=False)
    g, j, t = best_split(X, y, columns)
    if j is None:
        return {"leaf": majority}
    left = X[:, j] <= t
    return {"feature": j, "threshold": t,
            "left": grow(X[left], y[left], max_depth, max_features, rng, depth + 1),
            "right": grow(X[~left], y[~left], max_depth, max_features, rng, depth + 1)}

def predict(node, X):
    out = []
    for x in X:
        n = node
        while "leaf" not in n:
            n = n["left"] if x[n["feature"]] <= n["threshold"] else n["right"]
        out.append(n["leaf"])
    return np.array(out)
