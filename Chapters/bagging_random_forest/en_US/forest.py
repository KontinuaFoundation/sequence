import numpy as np
from penguins import load_penguins
from trees import grow, predict

data = load_penguins()
names, y = np.unique(data["species"], return_inverse=True)
features = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
X = np.column_stack([data[f] for f in features])
order = np.random.default_rng(1).permutation(len(y))
dev, test = order[:266], order[266:]
X_dev, y_dev, n = X[dev], y[dev], len(dev)

def forest(n_trees, max_features, seed=0):
    rng = np.random.default_rng(seed)
    test_votes = np.zeros((len(test), 3))
    oob_votes = np.zeros((n, 3))
    single = []                                  # accuracy of each tree alone
    for b in range(1, n_trees + 1):
        sample = rng.integers(0, n, size=n)      # bootstrap: n draws with replacement
        tree = grow(X_dev[sample], y_dev[sample], max_features=max_features, rng=rng)
        guess = predict(tree, X[test])
        test_votes[np.arange(len(test)), guess] += 1
        single.append(np.mean(guess == y[test]))
        out = np.setdiff1d(np.arange(n), sample)   # penguins this tree never saw
        oob_votes[out, predict(tree, X_dev[out])] += 1
        if b in (1, 10, 50, 200):
            seen = oob_votes.sum(axis=1) > 0
            oob = np.mean(oob_votes[seen].argmax(axis=1) == y_dev[seen])
            acc = np.mean(test_votes.argmax(axis=1) == y[test])
            print(f"  {b:3d} trees: out-of-bag {oob:.3f}, test {acc:.3f}")
    print(f"  single trees on the test set: {min(single):.3f} to {max(single):.3f},"
          f" average {np.mean(single):.3f}")

print("Bagging (every split sees all 4 features)")
forest(200, max_features=None)
print("Random forest (every split sees 2 random features)")
forest(200, max_features=2)
