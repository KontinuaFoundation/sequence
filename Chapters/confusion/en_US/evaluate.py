import numpy as np
from penguins import load_penguins

data = load_penguins()
y = (data["species"] == "Chinstrap").astype(int)     # 1 = Chinstrap
features = np.column_stack([data["bill_length_mm"], data["bill_depth_mm"]])
n = len(y)

order = np.random.default_rng(1).permutation(n)
train, test = order[:233], order[233:]
mean, sd = features[train].mean(axis=0), features[train].std(axis=0)
X = np.column_stack([np.ones(n), (features - mean) / sd])

# Logistic regression, as in the last chapter
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

theta = np.zeros(3)
for _ in range(3000):
    p = sigmoid(X[train] @ theta)
    theta = theta - 0.5 * X[train].T @ (p - y[train]) / len(train)

scores = sigmoid(X[test] @ theta)       # P(Chinstrap) for each test penguin
actual = y[test]
print(f"Test penguins: {len(actual)}, Chinstraps: {actual.sum()}")

def confusion(actual, predicted):
    tp = np.sum((predicted == 1) & (actual == 1))
    fp = np.sum((predicted == 1) & (actual == 0))
    fn = np.sum((predicted == 0) & (actual == 1))
    tn = np.sum((predicted == 0) & (actual == 0))
    return tp, fp, fn, tn

tp, fp, fn, tn = confusion(actual, (scores >= 0.5).astype(int))
print(f"TP={tp} FP={fp} FN={fn} TN={tn}")
print(f"accuracy  {(tp + tn) / len(actual):.2f}")
print(f"precision {tp / (tp + fp):.2f}")
print(f"recall    {tp / (tp + fn):.2f}")

# Sweep the threshold
print("threshold  TP  FP  FN  TN  precision  recall")
for threshold in [0.1, 0.2, 0.3, 0.5, 0.7, 0.9]:
    tp, fp, fn, tn = confusion(actual, (scores >= threshold).astype(int))
    print(f"{threshold:9.1f} {tp:3d} {fp:3d} {fn:3d} {tn:3d}"
          f"  {tp / (tp + fp):9.2f}  {tp / (tp + fn):6.2f}")

# ROC curve: lower the threshold past each score in turn
ranked = actual[np.argsort(-scores)]          # labels, highest score first
tpr = np.concatenate([[0], np.cumsum(ranked) / ranked.sum()])
fpr = np.concatenate([[0], np.cumsum(1 - ranked) / (1 - ranked).sum()])
print(f"AUC (area)  = {np.trapezoid(tpr, fpr):.3f}")

# AUC as the fraction of (positive, negative) pairs ranked correctly
pos, neg = scores[actual == 1], scores[actual == 0]
print(f"AUC (pairs) = {np.mean(pos[:, None] > neg[None, :]):.3f}")
