"""Author tool: draws the figures for this chapter."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from penguins import load_penguins
from trees import grow, predict

plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
BLUE, RED, GRAY = "#005FC6", "#C0392B", "#9a9a9a"

# Majority vote of independent voters
voters = np.arange(1, 102, 2)
fig, ax = plt.subplots(figsize=(5.5, 3))
for p, color in [(0.6, GRAY), (0.7, BLUE), (0.8, RED)]:
    ax.plot(voters, stats.binom.sf(voters // 2, voters, p), color=color, lw=2,
            label=f"each voter right {p:.0%}")
ax.set_xlabel("Number of independent voters")
ax.set_ylabel("P(majority is right)")
ax.legend(frameon=False, fontsize=9)
fig.tight_layout()
fig.savefig("crowd.png", dpi=200)

# Out-of-bag accuracy against number of trees
data = load_penguins()
names, y = np.unique(data["species"], return_inverse=True)
X = np.column_stack([data[f] for f in ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]])
order = np.random.default_rng(1).permutation(len(y))
dev = order[:266]
Xd, yd, n = X[dev], y[dev], len(dev)
fig, ax = plt.subplots(figsize=(5.5, 3))
for mf, color, label in [(None, BLUE, "bagging"), (2, RED, "random forest")]:
    rng = np.random.default_rng(0)
    votes = np.zeros((n, 3))
    curve = []
    for b in range(200):
        s = rng.integers(0, n, n)
        t = grow(Xd[s], yd[s], max_features=mf, rng=rng)
        out = np.setdiff1d(np.arange(n), s)
        votes[out, predict(t, Xd[out])] += 1
        seen = votes.sum(1) > 0
        curve.append(np.mean(votes[seen].argmax(1) == yd[seen]))
    ax.plot(range(1, 201), curve, color=color, lw=1.8, label=label)
ax.set_xscale("log")
ax.set_xticks([1, 3, 10, 30, 100, 200], ["1", "3", "10", "30", "100", "200"])
ax.set_xlabel("Number of trees (log scale)")
ax.set_ylabel("Out-of-bag accuracy")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("oob_trees.png", dpi=200)
