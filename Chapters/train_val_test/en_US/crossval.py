import numpy as np
from penguins import load_penguins

data = load_penguins()
x = data["flipper_length_mm"]
y = data["body_mass_g"]

rng = np.random.default_rng(seed=1)
order = rng.permutation(len(x))
n_test = 50
test, train = order[:n_test], order[n_test:]   # lock the test set away

mean, sd = x[train].mean(), x[train].std()
z = (x - mean) / sd

def rmse(actual, predicted):
    return np.sqrt(np.mean((actual - predicted)**2))

k = 5
folds = np.array_split(train, k)        # 5 groups of training rows

print("degree  cross-validated RMSE")
scores = {}
for degree in range(1, 6):
    errors = []
    for i in range(k):
        held_out = folds[i]
        fit_rows = np.concatenate([folds[j] for j in range(k) if j != i])
        coefficients = np.polyfit(z[fit_rows], y[fit_rows], degree)
        errors.append(rmse(y[held_out], np.polyval(coefficients, z[held_out])))
    scores[degree] = np.mean(errors)
    print(f"{degree:6d} {scores[degree]:12.1f}")

best = min(scores, key=scores.get)
coefficients = np.polyfit(z[train], y[train], best)
print(f"Chose degree {best}. Test RMSE: {rmse(y[test], np.polyval(coefficients, z[test])):.1f}")
