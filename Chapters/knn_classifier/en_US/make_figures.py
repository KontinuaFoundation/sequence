"""Author tool: draws the figures for this chapter."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from penguins import load_penguins

plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
COLORS = ["#FF8C00", "#A034F0", "#057076"]
BLUE, RED = "#005FC6", "#C0392B"

data = load_penguins()
names, y = np.unique(data["species"], return_inverse=True)
F = np.column_stack([data["bill_length_mm"], data["bill_depth_mm"]])
n = len(y)
order = np.random.default_rng(1).permutation(n)
dev, test = order[:266], order[266:]

def knn(Ftr, ytr, Fq, k):
    mu, sd = Ftr.mean(0), Ftr.std(0)
    A, Q = (Ftr - mu) / sd, (Fq - mu) / sd
    out = []
    for start in range(0, len(Q), 2000):
        D = np.sum((Q[start:start + 2000, None, :] - A[None, :, :])**2, axis=2)
        votes = ytr[np.argsort(D, axis=1)[:, :k]]
        out.append([np.bincount(r, minlength=3).argmax() for r in votes])
    return np.concatenate(out)

# Decision regions
gx, gy = np.meshgrid(np.linspace(31, 61, 300), np.linspace(12.5, 22, 300))
grid = np.column_stack([gx.ravel(), gy.ravel()])
fig, axes = plt.subplots(1, 3, figsize=(10, 3.4), sharey=True)
for ax, k in zip(axes, [1, 15, 101]):
    regions = knn(F[dev], y[dev], grid, k).reshape(gx.shape)
    ax.contourf(gx, gy, regions, levels=[-0.5, 0.5, 1.5, 2.5], cmap=ListedColormap(COLORS), alpha=0.25)
    for c in range(3):
        m = y[dev] == c
        ax.scatter(F[dev][m, 0], F[dev][m, 1], s=8, color=COLORS[c], label=names[c])
    ax.set_title(f"k = {k}", fontsize=11)
    ax.set_xlabel("Bill length (mm)")
axes[0].set_ylabel("Bill depth (mm)")
axes[2].legend(frameon=False, fontsize=8, loc="lower right")
fig.tight_layout()
fig.savefig("regions.png", dpi=200)

# Accuracy against k
folds = np.array_split(dev, 5)
ks = [1, 3, 5, 7, 9, 11, 15, 21, 31, 41, 51, 75, 101, 151]
cv, tr = [], []
for k in ks:
    accs = []
    for i in range(5):
        v = folds[i]
        t = np.concatenate([folds[j] for j in range(5) if j != i])
        accs.append(np.mean(knn(F[t], y[t], F[v], k) == y[v]))
    cv.append(np.mean(accs))
    tr.append(np.mean(knn(F[dev], y[dev], F[dev], k) == y[dev]))
fig, ax = plt.subplots(figsize=(6, 3.2))
ax.plot(ks, tr, "-o", color=BLUE, ms=4, label="training accuracy")
ax.plot(ks, cv, "-o", color=RED, ms=4, label="cross-validation accuracy")
ax.set_xscale("log")
ax.set_xticks([1, 3, 10, 30, 100], ["1", "3", "10", "30", "100"])
ax.set_xlabel("k (log scale)")
ax.set_ylabel("Accuracy")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("accuracy_k.png", dpi=200)
