import numpy as np

# Simulated data: customers at a smoothie shop between 3 and 4 p.m. on 120 days
rng = np.random.default_rng(7)
n = 120
temp = rng.uniform(0, 32, n)                       # afternoon temperature, degrees C
weekend = (rng.random(n) < 2 / 7).astype(float)
true_beta = np.array([0.3, 0.07, 0.5])             # intercept, temperature, weekend
X = np.column_stack([np.ones(n), temp, weekend])
customers = rng.poisson(np.exp(X @ true_beta))

# Poisson regression by iteratively reweighted least squares (Newton's method)
beta = np.array([np.log(customers.mean()), 0, 0])   # start: every day average
for step in range(1, 7):
    mu = np.exp(X @ beta)                          # current predicted means
    gradient = X.T @ (customers - mu)
    hessian = X.T @ (mu[:, None] * X)              # X^T W X with W = diag(mu)
    beta = beta + np.linalg.solve(hessian, gradient)
    print(f"step {step}: beta = {np.round(beta, 4)}")

print("multipliers e^beta:", np.round(np.exp(beta), 3))

# Compare with an ordinary least squares line
b_ls, *_ = np.linalg.lstsq(X, customers)
cold_weekday = np.array([1, 0, 0])
hot_weekend = np.array([1, 32, 1])
for name, x in [("0 C weekday", cold_weekday), ("32 C weekend", hot_weekend)]:
    print(f"{name}: Poisson {np.exp(x @ beta):5.1f}, least squares {x @ b_ls:5.1f}")
