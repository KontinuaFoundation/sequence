import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])
X = np.column_stack([np.ones(len(x)), x])

def descend(alpha, steps):
    theta = np.zeros(2)
    for _ in range(steps):
        gradient = 2 / len(y) * X.T @ (X @ theta - y)
        theta = theta - alpha * gradient
    return theta

print(descend(0.05, 50))
print(descend(0.05, 5000))
print(descend(0.1, 50))
