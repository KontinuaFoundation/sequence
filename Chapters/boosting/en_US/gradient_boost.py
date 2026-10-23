import numpy as np
from penguins import load_penguins

data = load_penguins()
y = data["body_mass_g"]
data["male"] = (data["sex"] == "male").astype(float)
data["gentoo"] = (data["species"] == "Gentoo").astype(float)
data["chinstrap"] = (data["species"] == "Chinstrap").astype(float)
features = ["flipper_length_mm", "bill_length_mm", "bill_depth_mm",
            "male", "gentoo", "chinstrap"]
X = np.column_stack([data[f] for f in features])
order = np.random.default_rng(1).permutation(len(y))
train, test = order[:233], order[233:]

def fit_stump(X, r):
    """The one-question rule that best predicts the residuals r (least squares)."""
    best = (np.inf, None, None, None, None)
    for j in range(X.shape[1]):
        values = np.unique(X[:, j])
        for t in (values[:-1] + values[1:]) / 2:
            left = X[:, j] <= t
            mean_left, mean_right = r[left].mean(), r[~left].mean()
            sse = np.sum((r[left] - mean_left)**2) + np.sum((r[~left] - mean_right)**2)
            if sse < best[0]:
                best = (sse, j, t, mean_left, mean_right)
    return best

def stump_predict(stump, X):
    _, j, t, mean_left, mean_right = stump
    return np.where(X[:, j] <= t, mean_left, mean_right)

def rmse(pred, rows):
    return np.sqrt(np.mean((y[rows] - pred)**2))

rate = 0.1
pred_train = np.full(len(train), y[train].mean())    # start with the average
pred_test = np.full(len(test), y[train].mean())
for t in range(1, 501):
    residuals = y[train] - pred_train
    stump = fit_stump(X[train], residuals)
    pred_train += rate * stump_predict(stump, X[train])
    pred_test += rate * stump_predict(stump, X[test])
    if t in (1, 10, 50, 100, 200, 500):
        print(f"{t:3d} stumps: training RMSE {rmse(pred_train, train):.0f}, "
              f"test RMSE {rmse(pred_test, test):.0f}")
