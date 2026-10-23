"""Author tool: draws the figures for this chapter."""
import numpy as np
import matplotlib.pyplot as plt
from penguins import load_penguins

plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
COLORS = {"Adelie": "#FF8C00", "Chinstrap": "#A034F0", "Gentoo": "#057076"}
data = load_penguins()
species = data["species"]

def line(x, y):
    b1 = np.sum((x - x.mean()) * (y - y.mean())) / np.sum((x - x.mean())**2)
    return y.mean() - b1 * x.mean(), b1

# Quiz data with residuals drawn as squares
x = np.array([1, 2, 3, 4, 5.0])
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])
b0, b1 = line(x, y)
fig, ax = plt.subplots(figsize=(5, 3.6))
xs = np.linspace(0.5, 5.5, 2)
ax.plot(xs, b0 + b1 * xs, color="#005FC6", lw=2)
for xi, yi in zip(x, y):
    yh = b0 + b1 * xi
    ax.plot([xi, xi], [yi, yh], color="#C0392B", lw=1.5)
    ax.text(xi + 0.08, (yi + yh) / 2, f"{yi - yh:+.2f}", color="#C0392B", fontsize=9, va="center")
ax.scatter(x, y, color="black", zorder=3)
ax.set_xlabel("Hours studied")
ax.set_ylabel("Quiz score")
ax.set_xlim(0.5, 5.8)
fig.tight_layout()
fig.savefig("quiz_residuals.png", dpi=200)

# Penguin line
f, m = data["flipper_length_mm"], data["body_mass_g"]
b0, b1 = line(f, m)
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(f, m, s=12, color="#9a9a9a")
xs = np.array([f.min() - 2, f.max() + 2])
ax.plot(xs, b0 + b1 * xs, color="#005FC6", lw=2)
ax.set_xlabel("Flipper length (mm)")
ax.set_ylabel("Body mass (g)")
ax.text(176, 5800, f"mass = {b0:.0f} + {b1:.2f} $\\times$ flipper", color="#005FC6")
fig.tight_layout()
fig.savefig("penguin_line.png", dpi=200)

# Residuals by species
res = m - (b0 + b1 * f)
fig, ax = plt.subplots(figsize=(6, 3.4))
for s, c in COLORS.items():
    k = species == s
    ax.scatter(f[k], res[k], s=12, color=c, label=s)
ax.axhline(0, color="black", lw=1)
ax.set_xlabel("Flipper length (mm)")
ax.set_ylabel("Residual (g)")
ax.legend(frameon=False, fontsize=9)
fig.tight_layout()
fig.savefig("residuals_species.png", dpi=200)

# Simpson's paradox: bill depth
d = data["bill_depth_mm"]
fig, ax = plt.subplots(figsize=(6, 4))
for s, c in COLORS.items():
    k = species == s
    ax.scatter(d[k], m[k], s=12, color=c, label=s)
    a0, a1 = line(d[k], m[k])
    xs = np.array([d[k].min(), d[k].max()])
    ax.plot(xs, a0 + a1 * xs, color=c, lw=2)
a0, a1 = line(d, m)
xs = np.array([d.min(), d.max()])
ax.plot(xs, a0 + a1 * xs, color="black", lw=2, ls="--", label="all penguins")
ax.set_xlabel("Bill depth (mm)")
ax.set_ylabel("Body mass (g)")
ax.legend(frameon=False, fontsize=9)
fig.tight_layout()
fig.savefig("simpson.png", dpi=200)
