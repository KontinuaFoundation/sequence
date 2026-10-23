"""Author tool: draws the figures for this chapter."""
import numpy as np
import matplotlib.pyplot as plt
from penguins import load_penguins

plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
BLUE, RED, GRAY, ORANGE = "#005FC6", "#C0392B", "#9a9a9a", "#FF8C00"

x = np.array([1, 2, 3, 4, 5.0])
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])
X = np.column_stack([np.ones(5), x])

def path(alpha, steps):
    theta = np.zeros(2)
    out = [theta]
    for _ in range(steps):
        theta = theta - alpha * 2 / 5 * X.T @ (X @ theta - y)
        out.append(theta)
    return np.array(out)

def cost(t0, t1):
    return np.mean((t0[..., None] + t1[..., None] * x - y)**2, axis=-1)

# Contour plot with two paths
t0, t1 = np.meshgrid(np.linspace(-0.6, 1.4, 300), np.linspace(-0.1, 3.7, 300))
fig, ax = plt.subplots(figsize=(6, 4))
ax.contour(t0, t1, cost(t0, t1), levels=[0.03, 0.1, 0.3, 1, 3, 10, 30], colors=GRAY, linewidths=0.8)
p = path(0.01, 400)
ax.plot(p[:, 0], p[:, 1], "-", color=BLUE, lw=2, label="$\\alpha = 0.01$, 400 steps")
p = path(0.08, 12)
ax.plot(p[:, 0], p[:, 1], "-o", color=RED, ms=3.5, lw=1, label="$\\alpha = 0.08$, 12 steps")
ax.plot([0.05], [1.99], "*", color="black", ms=12)
ax.set_xlabel(r"$\theta_0$ (intercept)")
ax.set_ylabel(r"$\theta_1$ (slope)")
ax.legend(frameon=False, loc="lower left")
fig.tight_layout()
fig.savefig("contour_paths.png", dpi=200)

# Cost against step for several learning rates
fig, ax = plt.subplots(figsize=(6, 3.4))
for alpha, color in [(0.001, GRAY), (0.01, BLUE), (0.08, ORANGE), (0.09, RED)]:
    p = path(alpha, 100)
    ax.plot(cost(p[:, 0], p[:, 1]), color=color, lw=2, label=f"$\\alpha = {alpha}$")
ax.set_yscale("log")
ax.set_ylim(0.01, 1000)
ax.set_xlabel("Step")
ax.set_ylabel("Cost $J$ (log scale)")
ax.legend(frameon=False, ncol=2)
fig.tight_layout()
fig.savefig("learning_rates.png", dpi=200)

# Full-batch versus mini-batch cost, penguins (standardized flipper)
data = load_penguins()
f, m = data["flipper_length_mm"], data["body_mass_g"]
n = len(m)
Z = np.column_stack([np.ones(n), (f - f.mean()) / f.std()])
rmse = lambda t: np.sqrt(np.mean((Z @ t - m)**2))
full = []
theta = np.zeros(2)
for _ in range(6):
    full.append(rmse(theta))
    theta = theta - 0.1 * 2 / n * Z.T @ (Z @ theta - m)
rng = np.random.default_rng(0)
theta = np.zeros(2)
mini, when = [rmse(theta)], [0]
for epoch in range(5):
    order = rng.permutation(n)
    for start in range(0, n, 32):
        rows = order[start:start + 32]
        theta = theta - 0.1 * 2 / len(rows) * Z[rows].T @ (Z[rows] @ theta - m[rows])
        mini.append(rmse(theta))
        when.append(epoch + min(start + 32, n) / n)
fig, ax = plt.subplots(figsize=(6, 3.2))
ax.plot(range(6), full, "-o", color=BLUE, lw=2, label="full batch: 1 step per pass")
ax.plot(when, mini, "-", color=RED, lw=1.5, label="mini-batches of 32: 11 steps per pass")
ax.set_yscale("log")
ax.set_yticks([400, 1000, 2000, 4000], ["400", "1000", "2000", "4000"])
ax.set_yticks([], minor=True)
ax.set_xlabel("Passes through the data (epochs)")
ax.set_ylabel("RMSE on all penguins (g)")
ax.legend(frameon=False, loc="center right")
fig.tight_layout()
fig.savefig("minibatch.png", dpi=200)
