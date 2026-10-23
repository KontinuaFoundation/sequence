import numpy as np
from scipy import stats
from penguins import load_penguins

data = load_penguins()
names, y = np.unique(data["species"], return_inverse=True)
features = np.column_stack([data["bill_length_mm"], data["bill_depth_mm"]])
order = np.random.default_rng(1).permutation(len(y))
dev, test = order[:266], order[266:]

def fit(rows):
    """For each species: prior, mean vector, and covariance matrix."""
    model = []
    for c in range(3):
        group = features[rows][y[rows] == c]
        model.append((len(group) / len(rows), group.mean(axis=0),
                      np.cov(group.T, bias=True)))
    return model

def log_posteriors(model, X, naive):
    scores = []
    for prior, mean, cov in model:
        if naive:   # independent normal distributions, one per feature
            sd = np.sqrt(np.diag(cov))
            log_like = stats.norm.logpdf(X, mean, sd).sum(axis=1)
        else:       # one multivariate normal, with covariance
            log_like = stats.multivariate_normal.logpdf(X, mean, cov)
        scores.append(np.log(prior) + log_like)
    return np.column_stack(scores)

def probabilities(scores):
    p = np.exp(scores - scores.max(axis=1, keepdims=True))
    return p / p.sum(axis=1, keepdims=True)

folds = np.array_split(dev, 5)
model = fit(dev)
mystery = np.array([[45.0, 17.0]])        # bill length 45 mm, depth 17 mm
for naive in (True, False):
    accuracy = []
    for i in range(5):
        rest = np.concatenate([folds[j] for j in range(5) if j != i])
        scores = log_posteriors(fit(rest), features[folds[i]], naive)
        accuracy.append(np.mean(scores.argmax(axis=1) == y[folds[i]]))
    guess = log_posteriors(model, features[test], naive).argmax(axis=1)
    test_acc = np.mean(guess == y[test])
    p = probabilities(log_posteriors(model, mystery, naive))
    print("naive" if naive else "full ", f"CV {np.mean(accuracy):.3f}",
          f"test {test_acc:.3f}  mystery:", np.round(p, 3))
