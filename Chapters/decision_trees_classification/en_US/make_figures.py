"""Author tool: draws the figures for this chapter."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
COLORS = ["#FF8C00", "#A034F0", "#057076"]
BLUE, RED, GRAY = "#005FC6", "#C0392B", "#9a9a9a"

src = open("tree.py").read().split("tree = grow(X[dev], y[dev], 0, max_depth=2)")[0]
exec(src)

# Impurity curves for two classes
p = np.linspace(0.001, 0.999, 300)
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(p, 1 - p**2 - (1 - p)**2, color=BLUE, lw=2, label="Gini impurity")
ax.plot(p, -(p * np.log2(p) + (1 - p) * np.log2(1 - p)), color=RED, lw=2, label="entropy (bits)")
ax.set_xlabel("Fraction of the node in class A")
ax.set_ylabel("Impurity")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("impurity.png", dpi=200)

# Regions for trees on two features
X2 = X[:, [2, 0]]          # flipper length, bill length
gx, gy = np.meshgrid(np.linspace(170, 235, 400), np.linspace(31, 61, 400))
grid = np.column_stack([gx.ravel(), gy.ravel()])
fig, axes = plt.subplots(1, 2, figsize=(9, 3.6), sharey=True)
for ax, depth in zip(axes, [2, 10]):
    t = grow(X2[dev], y[dev], 0, depth)
    regions = predict(t, grid).reshape(gx.shape)
    ax.contourf(gx, gy, regions, levels=[-0.5, 0.5, 1.5, 2.5], cmap=ListedColormap(COLORS), alpha=0.25)
    for c in range(3):
        m = y[dev] == c
        ax.scatter(X2[dev][m, 0], X2[dev][m, 1], s=7, color=COLORS[c], label=names[c])
    ax.set_title(f"max depth {depth}", fontsize=11)
    ax.set_xlabel("Flipper length (mm)")
axes[0].set_ylabel("Bill length (mm)")
axes[1].legend(frameon=False, fontsize=8, loc="lower right")
fig.tight_layout()
fig.savefig("tree_regions.png", dpi=200)

# Accuracy against depth
folds = np.array_split(dev, 5)
depths = range(1, 11)
tr, cv = [], []
for d in depths:
    t = grow(X[dev], y[dev], 0, d)
    tr.append(np.mean(predict(t, X[dev]) == y[dev]))
    a = []
    for i in range(5):
        r = np.concatenate([folds[j] for j in range(5) if j != i])
        a.append(np.mean(predict(grow(X[r], y[r], 0, d), X[folds[i]]) == y[folds[i]]))
    cv.append(np.mean(a))
fig, ax = plt.subplots(figsize=(5.5, 3))
ax.plot(depths, tr, "-o", color=BLUE, ms=4, label="training")
ax.plot(depths, cv, "-o", color=RED, ms=4, label="cross-validation")
ax.set_xlabel("Maximum depth")
ax.set_ylabel("Accuracy")
ax.set_ylim(0.78, 1.01)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("depth.png", dpi=200)
