import numpy as np
from scipy.optimize import minimize
from penguins import load_penguins

data = load_penguins()
adelie = data["species"] == "Adelie"
y = (data["sex"][adelie] == "male").astype(float)    # 1 = male, 0 = female
features = np.column_stack([data["body_mass_g"][adelie],
                            data["bill_depth_mm"][adelie]])
n = len(y)

order = np.random.default_rng(1).permutation(n)
train, test = order[:110], order[110:]

# Standardize with the training penguins' means and standard deviations
mean, sd = features[train].mean(axis=0), features[train].std(axis=0)
X = np.column_stack([np.ones(n), (features - mean) / sd])

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def log_loss(theta, rows):
    p = sigmoid(X[rows] @ theta)
    return -np.mean(y[rows] * np.log(p) + (1 - y[rows]) * np.log(1 - p))

theta = np.zeros(3)
alpha = 0.5
for step in range(1, 1001):
    p = sigmoid(X[train] @ theta)
    gradient = X[train].T @ (p - y[train]) / len(train)
    theta = theta - alpha * gradient
    if step in (1, 10, 100, 1000):
        print(f"step {step:4d}: loss {log_loss(theta, train):.4f}")

print("theta:", np.round(theta, 2))
for name, rows in [("train", train), ("test", test)]:
    predicted = sigmoid(X[rows] @ theta) >= 0.5
    print(f"{name} accuracy: {np.mean(predicted == y[rows]):.1%}")

# A new Adelie: 3600 g, bill depth 18.0 mm
x_new = np.concatenate([[1], (np.array([3600, 18.0]) - mean) / sd])
print(f"P(male) = {sigmoid(x_new @ theta):.2f}")

# Check against SciPy's general-purpose minimizer
result = minimize(log_loss, np.zeros(3), args=(train,))
print("SciPy theta:", np.round(result.x, 2))
