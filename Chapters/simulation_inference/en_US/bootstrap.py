import numpy as np

rng = np.random.default_rng(4)

# Hours of sleep reported by 20 randomly chosen students
sleep = np.array([6.5, 7.0, 5.5, 8.0, 6.0, 7.5, 6.5, 9.0, 5.0, 7.0,
                  6.0, 8.5, 7.0, 6.5, 4.5, 7.5, 6.0, 7.0, 8.0, 6.5])
n = len(sleep)
print(f"sample mean: {sleep.mean():.3f}")

# 10,000 bootstrap samples: n values drawn WITH replacement from the sample
resamples = rng.choice(sleep, size=(10_000, n), replace=True)
boot_means = resamples.mean(axis=1)

low, high = np.percentile(boot_means, [2.5, 97.5])
print(f"bootstrap SE: {boot_means.std():.3f}")
print(f"s / sqrt(n):  {sleep.std(ddof=1) / np.sqrt(n):.3f}")
print(f"95% bootstrap interval: ({low:.2f}, {high:.2f})")
