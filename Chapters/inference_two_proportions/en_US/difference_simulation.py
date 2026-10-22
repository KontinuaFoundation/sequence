import numpy as np

rng = np.random.default_rng(3)
p1, n1 = 0.35, 240        # juniors
p2, n2 = 0.27, 200        # seniors

# 10,000 pairs of surveys
p_hat_1 = rng.binomial(n1, p1, size=10_000) / n1
p_hat_2 = rng.binomial(n2, p2, size=10_000) / n2
diff = p_hat_1 - p_hat_2

theory = np.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
print(f"mean of differences: {diff.mean():.4f}  (p1 - p2 = {p1 - p2:.2f})")
print(f"sd of differences:   {diff.std():.4f}  (formula: {theory:.4f})")
print(f"sd if you subtracted the sds: {abs(np.sqrt(p1*(1-p1)/n1) - np.sqrt(p2*(1-p2)/n2)):.4f}")
