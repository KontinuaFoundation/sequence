"""Author tool: draws the figures for this chapter."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
BLUE, RED, GRAY = "#005FC6", "#C0392B", "#9a9a9a"

# Splitting one point's deviation into explained and unexplained parts
x = np.array([0, 1, 2, 3.0])
y = np.array([1, 3, 4, 8.0])
y_hat = 0.7 + 2.2 * x
fig, ax = plt.subplots(figsize=(5.2, 3.8))
xs = np.array([-0.3, 3.25])
ax.plot(xs, 0.7 + 2.2 * xs, color=BLUE, lw=2, label="least squares line")
ax.axhline(y.mean(), color=GRAY, lw=1.5, ls="--", label=r"mean, $\bar{y} = 4$")
ax.scatter(x, y, color="black", zorder=3)
i = 3
ax.plot([x[i] - 0.04] * 2, [y.mean(), y[i]], color="black", lw=1.5)
ax.plot([x[i] + 0.04] * 2, [y.mean(), y_hat[i]], color=BLUE, lw=3)
ax.plot([x[i] + 0.04] * 2, [y_hat[i], y[i]], color=RED, lw=3)
ax.annotate(r"$y_i - \bar{y} = 4$", (x[i] - 0.08, 7.75), ha="right")
ax.annotate(r"$\hat{y}_i - \bar{y} = 3.3$", (x[i] + 0.1, 5.5), color=BLUE)
ax.annotate(r"$y_i - \hat{y}_i = 0.7$", (x[i] + 0.1, 8.3), color=RED)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_xlim(-0.3, 4.2)
ax.set_ylim(-0.3, 9)
ax.legend(frameon=False, fontsize=9, loc="upper left")
fig.tight_layout()
fig.savefig("ss_split.png", dpi=200)

# Stopping distance (simulated): high R^2, wrong shape
rng = np.random.default_rng(3)
v = np.arange(20, 72, 2.0)
d = 0.2 * v + v**2 / 120 + rng.normal(0, 1.5, len(v))
A = np.column_stack([np.ones(len(v)), v])
b, *_ = np.linalg.lstsq(A, d)
res = d - A @ b
fig, axes = plt.subplots(1, 2, figsize=(8, 3))
axes[0].scatter(v, d, s=14, color="black")
axes[0].plot(v, A @ b, color=BLUE, lw=2)
axes[0].set_xlabel("Speed (km/h)")
axes[0].set_ylabel("Stopping distance (m)")
axes[1].scatter(v, res, s=14, color=RED)
axes[1].axhline(0, color="black", lw=1)
axes[1].set_xlabel("Speed (km/h)")
axes[1].set_ylabel("Residual (m)")
fig.tight_layout()
fig.savefig("stopping.png", dpi=200)

# The F distribution with 1 and 3 degrees of freedom
fs = np.linspace(0.05, 16, 400)
crit = stats.f.ppf(0.95, 1, 3)
fig, ax = plt.subplots(figsize=(5.5, 2.8))
ax.plot(fs, stats.f.pdf(fs, 1, 3), color=BLUE, lw=2)
tail = fs >= crit
ax.fill_between(fs[tail], stats.f.pdf(fs[tail], 1, 3), color=RED, alpha=0.4)
ax.axvline(crit, color=RED, lw=1, ls="--")
ax.annotate(f"top 5%: F > {crit:.2f}", (crit + 0.3, 0.1), color=RED)
ax.set_xlabel("F")
ax.set_ylabel("Density")
ax.set_ylim(0, 0.5)
fig.tight_layout()
fig.savefig("f_dist.png", dpi=200)
