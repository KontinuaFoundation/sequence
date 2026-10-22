import numpy as np

rng = np.random.default_rng(2)
p = 0.55             # true support for the candidate

for n in [100, 1000]:
    # 10,000 polls of n voters; p-hat is the fraction who say yes
    p_hat = rng.binomial(n, p, size=10_000) / n
    wrong = np.mean(p_hat < 0.5)
    print(f"n = {n:4}: mean {p_hat.mean():.3f}, sd {p_hat.std():.4f}, "
          f"polls showing a loss: {wrong:.4f}")
