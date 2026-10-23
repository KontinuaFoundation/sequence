"""Author tool: draws the overfitting figures for this chapter."""
import numpy as np
import matplotlib.pyplot as plt
from penguins import load_penguins

BLUE, GRAY, RED = "#005FC6", "#9a9a9a", "#C0392B"
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
data = load_penguins()
x, y = data["flipper_length_mm"], data["body_mass_g"]
order = np.random.default_rng(seed=4).permutation(len(x))
train, val = order[:12], order[12:62]
mean, sd = x[train].mean(), x[train].std()
z = (x - mean) / sd
grid = np.linspace(x.min(), x.max(), 400)

fig, axes = plt.subplots(1, 3, figsize=(10, 3.4), sharey=True)
for ax, degree in zip(axes, [1, 3, 8]):
    c = np.polyfit(z[train], y[train], degree)
    ax.scatter(x[val], y[val], s=12, color=GRAY, label="validation penguins")
    ax.scatter(x[train], y[train], s=28, color=BLUE, label="training penguins", zorder=3)
    ax.plot(grid, np.polyval(c, (grid - mean) / sd), color=RED, lw=2)
    ax.set_ylim(2500, 6500)
    ax.set_title(f"degree {degree}")
    ax.set_xlabel("Flipper length (mm)")
axes[0].set_ylabel("Body mass (g)")
axes[0].legend(frameon=False, fontsize=9, loc="upper left")
fig.tight_layout()
fig.savefig("overfit_fits.png", dpi=200)

def rmse(a, b):
    return np.sqrt(np.mean((a - b) ** 2))
degrees = range(1, 9)
tr, va = [], []
for degree in degrees:
    c = np.polyfit(z[train], y[train], degree)
    tr.append(rmse(y[train], np.polyval(c, z[train])))
    va.append(rmse(y[val], np.polyval(c, z[val])))
fig, ax = plt.subplots(figsize=(6, 3.6))
ax.plot(degrees, tr, "o-", color=BLUE, label="training RMSE")
ax.plot(degrees, va, "s-", color=RED, label="validation RMSE")
ax.set_yscale("log")
ax.set_xlabel("Polynomial degree")
ax.set_ylabel("RMSE (g, log scale)")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("overfit_curve.png", dpi=200)
