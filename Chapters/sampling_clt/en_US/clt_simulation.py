import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

rng = np.random.default_rng(1)
MEAN = 10            # average watch time, in minutes
SAMPLES = 10_000     # how many samples we draw for each size

fig, axes = plt.subplots(1, 3, figsize=(10, 3))
for ax, n in zip(axes, [1, 5, 30]):
    # 10,000 samples of n watch times each; average each sample
    data = rng.exponential(MEAN, size=(SAMPLES, n))
    means = data.mean(axis=1)
    print(f"n = {n:2}: mean of x-bar = {means.mean():.2f}, "
          f"sd of x-bar = {means.std():.2f}, theory = {MEAN / np.sqrt(n):.2f}")

    ax.hist(means, bins=50, density=True, color="#005892")
    x = np.linspace(0, means.max(), 300)
    ax.plot(x, norm.pdf(x, MEAN, MEAN / np.sqrt(n)), color="orange")
    ax.set_title(f"sample size n = {n}")
    ax.set_xlabel("sample mean (minutes)")
fig.tight_layout()
fig.savefig("clt_simulation.png")
