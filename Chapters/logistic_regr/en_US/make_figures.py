"""Author tool: draws the figures for this chapter."""
import numpy as np
import matplotlib.pyplot as plt
from penguins import load_penguins

plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
BLUE, RED, GRAY = "#005FC6", "#C0392B", "#9a9a9a"
sigmoid = lambda z: 1 / (1 + np.exp(-z))

data = load_penguins()
a = data["species"] == "Adelie"
y = (data["sex"][a] == "male").astype(float)
mass, depth = data["body_mass_g"][a], data["bill_depth_mm"][a]
n = len(y)

def fit(F, steps=3000):
    mu, sd = F.mean(0), F.std(0)
    X = np.column_stack([np.ones(n), (F - mu) / sd])
    t = np.zeros(X.shape[1])
    for _ in range(steps):
        t -= 0.5 * X.T @ (sigmoid(X @ t) - y) / n
    b = t[1:] / sd
    return t[0] - b @ mu, b

# A line versus the S-curve, mass only
b0, b = fit(mass[:, None])
c1 = np.sum((mass - mass.mean()) * (y - y.mean())) / np.sum((mass - mass.mean())**2)
c0 = y.mean() - c1 * mass.mean()
jitter = np.random.default_rng(0).uniform(-0.03, 0.03, n)
xs = np.linspace(2500, 5000, 300)
fig, ax = plt.subplots(figsize=(6, 3.6))
ax.scatter(mass, y + jitter, s=12, color=np.where(y == 1, BLUE, RED), alpha=0.7)
ax.plot(xs, c0 + c1 * xs, color=GRAY, lw=2, ls="--", label="least squares line")
ax.plot(xs, sigmoid(b0 + b[0] * xs), color="black", lw=2, label="logistic regression")
ax.axhline(0, color=GRAY, lw=0.5)
ax.axhline(1, color=GRAY, lw=0.5)
ax.set_xlabel("Body mass (g)")
ax.set_ylabel("P(male)")
ax.set_yticks([-0.25, 0, 0.5, 1, 1.25])
ax.legend(frameon=False, loc="upper left", fontsize=9)
fig.tight_layout()
fig.savefig("line_vs_sigmoid.png", dpi=200)

# The sigmoid itself
z = np.linspace(-6, 6, 300)
fig, ax = plt.subplots(figsize=(5, 2.8))
ax.plot(z, sigmoid(z), color=BLUE, lw=2)
ax.axhline(0.5, color=GRAY, lw=0.8, ls="--")
ax.axvline(0, color=GRAY, lw=0.8, ls="--")
ax.set_xlabel("$z$ (log odds)")
ax.set_ylabel(r"$\sigma(z)$")
fig.tight_layout()
fig.savefig("sigmoid.png", dpi=200)

# Log loss for one example
p = np.linspace(0.005, 0.995, 300)
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(p, -np.log(p), color=BLUE, lw=2, label="truly male ($y = 1$): $-\\ln p$")
ax.plot(p, -np.log(1 - p), color=RED, lw=2, label="truly female ($y = 0$): $-\\ln(1 - p)$")
ax.set_xlabel("Predicted P(male)")
ax.set_ylabel("Loss")
ax.set_ylim(0, 5)
ax.legend(frameon=False, fontsize=9, loc="upper center")
fig.tight_layout()
fig.savefig("log_loss.png", dpi=200)

# Decision boundary with mass and bill depth
b0, b = fit(np.column_stack([mass, depth]))
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(mass[y == 1], depth[y == 1], s=14, color=BLUE, label="male")
ax.scatter(mass[y == 0], depth[y == 0], s=14, color=RED, marker="s", label="female")
ms = np.array([2800, 4800])
for prob, style in [(0.5, "-"), (0.1, ":"), (0.9, ":")]:
    logit = np.log(prob / (1 - prob))
    ax.plot(ms, (logit - b0 - b[0] * ms) / b[1], color="black", ls=style, lw=1.5 if prob == 0.5 else 1)
    m_at = (logit - b0 - b[1] * 15.8) / b[0]
    ax.text(m_at + 25, 15.6, f"{prob}", fontsize=10)
ax.set_xlim(2800, 4900)
ax.set_ylim(15.3, 21.8)
ax.set_xlabel("Body mass (g)")
ax.set_ylabel("Bill depth (mm)")
ax.legend(frameon=False, loc="upper left", fontsize=9)
fig.tight_layout()
fig.savefig("boundary.png", dpi=200)
