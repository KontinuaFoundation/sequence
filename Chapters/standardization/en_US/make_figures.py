"""Author tool: draws the figures for this chapter."""
import numpy as np
import matplotlib.pyplot as plt
from penguins import load_penguins

plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
data = load_penguins()
names = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
labels = ["bill length", "bill depth", "flipper length", "body mass"]
colors = ["#005FC6", "#7FB3E6", "#F4A261", "#C0392B"]
X = np.column_stack([data[n] for n in names])
Z = (X - X.mean(axis=0)) / X.std(axis=0)

# Share of the squared distance between penguin 91 and penguin 121 from each feature
fig, ax = plt.subplots(figsize=(6.4, 2.6))
for row, (M, title) in enumerate([(X, "raw units"), (Z, "standardized")]):
    sq = (M[91] - M[121]) ** 2
    share = 100 * sq / sq.sum()
    left = 0
    for k in range(4):
        ax.barh(row, share[k], left=left, color=colors[k], label=labels[k] if row == 0 else None)
        if share[k] > 6:
            ax.text(left + share[k] / 2, row, f"{share[k]:.1f}%" if share[k] > 99.5 else f"{share[k]:.0f}%", ha="center", va="center", color="white", fontsize=10)
        left += share[k]
ax.set_yticks([0, 1], ["raw units", "standardized"])
ax.invert_yaxis()
ax.set_xlim(0, 100)
ax.set_xlabel("Share of the squared distance (%)")
ax.legend(ncol=4, frameon=False, fontsize=9, loc="lower center", bbox_to_anchor=(0.5, 1.0))
fig.tight_layout()
fig.savefig("distance_shares.png", dpi=200)

# Standardizing changes the axis, not the shape
fig, axes = plt.subplots(1, 2, figsize=(8, 2.8))
axes[0].hist(X[:, 3], bins=25, color="#005FC6")
axes[0].set_xlabel("Body mass (g)")
axes[1].hist(Z[:, 3], bins=25, color="#C0392B")
axes[1].set_xlabel("Body mass (standardized)")
for ax in axes:
    ax.set_ylabel("Penguins")
fig.tight_layout()
fig.savefig("standardized_hist.png", dpi=200)
