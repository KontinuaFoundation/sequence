import numpy as np
from penguins import load_penguins

data = load_penguins()
names, y = np.unique(data["species"], return_inverse=True)   # y is 0, 1, or 2
features = np.column_stack([data["bill_length_mm"], data["bill_depth_mm"]])
n = len(y)

order = np.random.default_rng(1).permutation(n)
dev, test = order[:266], order[266:]       # 266 to develop with, 67 to test

def knn_predict(X_train, y_train, X_query, k):
    # Standardize using the training points only
    mean, sd = X_train.mean(axis=0), X_train.std(axis=0)
    A = (X_train - mean) / sd
    Q = (X_query - mean) / sd
    # Squared distance from every query point to every training point
    dist = np.sum((Q[:, None, :] - A[None, :, :])**2, axis=2)
    nearest = np.argsort(dist, axis=1)[:, :k]          # indices of the k closest
    votes = y_train[nearest]                            # their labels
    return np.array([np.bincount(row, minlength=3).argmax() for row in votes])

# 5-fold cross-validation on the development penguins
folds = np.array_split(dev, 5)
for k in [1, 3, 5, 15, 51, 101]:
    scores = []
    for i in range(5):
        val = folds[i]
        fit = np.concatenate([folds[j] for j in range(5) if j != i])
        predicted = knn_predict(features[fit], y[fit], features[val], k)
        scores.append(np.mean(predicted == y[val]))
    print(f"k = {k:3d}: cross-validation accuracy {np.mean(scores):.3f}")

# Final check with the chosen k
predicted = knn_predict(features[dev], y[dev], features[test], 3)
print(f"Test accuracy with k = 3: {np.mean(predicted == y[test]):.3f}")

matrix = np.zeros((3, 3), dtype=int)
for p, a in zip(predicted, y[test]):
    matrix[p, a] += 1
print("Rows: predicted, columns: actual", names)
print(matrix)
