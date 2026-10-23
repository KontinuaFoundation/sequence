import numpy as np
from penguins import load_penguins

data = load_penguins()
y = np.where(data["sex"] == "male", 1, -1)             # labels are +1 and -1
features = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
X = np.column_stack([data[f] for f in features])
order = np.random.default_rng(1).permutation(len(y))
train, test = order[:233], order[233:]

def best_stump(X, y, w):
    """The one-question rule with the smallest weighted error."""
    best = (np.inf, None, None, None)                 # (error, feature, threshold, sign)
    for j in range(X.shape[1]):
        values = np.unique(X[:, j])
        for t in (values[:-1] + values[1:]) / 2:
            guess = np.where(X[:, j] > t, 1, -1)
            for sign in (1, -1):                      # "big means male" or the reverse
                error = np.sum(w[sign * guess != y])
                if error < best[0]:
                    best = (error, j, t, sign)
    return best

def stump_predict(stump, X):
    _, j, t, sign = stump
    return sign * np.where(X[:, j] > t, 1, -1)

w = np.full(len(train), 1 / len(train))
score_train, score_test = np.zeros(len(train)), np.zeros(len(test))
for t in range(1, 201):
    stump = best_stump(X[train], y[train], w)
    error = stump[0]
    alpha = 0.5 * np.log((1 - error) / error)
    h = stump_predict(stump, X[train])
    w = w * np.exp(-alpha * y[train] * h)
    w = w / w.sum()
    score_train += alpha * h
    score_test += alpha * stump_predict(stump, X[test])
    if t <= 3:
        print(f"round {t}: {features[stump[1]]} > {stump[2]:.2f} means "
              f"{'male' if stump[3] == 1 else 'female'}; error {error:.3f}, alpha {alpha:.3f}")
    if t in (1, 10, 50, 200):
        acc_train = np.mean(np.sign(score_train) == y[train])
        acc_test = np.mean(np.sign(score_test) == y[test])
        print(f"{t:3d} stumps: training {acc_train:.3f}, test {acc_test:.3f}")
