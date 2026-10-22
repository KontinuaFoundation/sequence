import numpy as np

rng = np.random.default_rng(5)

# Quiz scores (out of 20) in a randomized experiment
silence = np.array([15, 17, 14, 16, 18, 13, 17, 15, 16, 19, 14, 16])
music   = np.array([13, 15, 12, 16, 14, 11, 15, 13, 17, 14, 12, 15])
observed = silence.mean() - music.mean()
print(f"observed difference: {observed:.3f}")

# If music makes no difference, the labels are meaningless: shuffle them.
scores = np.concatenate([silence, music])
diffs = np.empty(10_000)
for i in range(10_000):
    shuffled = rng.permutation(scores)
    diffs[i] = shuffled[:12].mean() - shuffled[12:].mean()

p_value = np.mean(diffs >= observed)
print(f"p-value: {p_value:.4f}")
