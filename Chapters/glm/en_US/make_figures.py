"""Author tool: draws the figures for this chapter."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
BLUE, RED, GRAY = "#005FC6", "#C0392B", "#9a9a9a"

# Poisson distributions with three means
k = np.arange(0, 31)
fig, ax = plt.subplots(figsize=(6, 2.8))
for mu, color in [(2, BLUE), (6, GRAY), (15, RED)]:
    ax.bar(k + {2: -0.27, 6: 0, 15: 0.27}[mu], stats.poisson.pmf(k, mu), width=0.27, color=color,
           label=f"mean {mu}")
ax.set_xlabel("Count")
ax.set_ylabel("Probability")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("poisson.png", dpi=200)

# The smoothie data with Poisson and least squares fits
ns = {}
exec(open("smoothies.py").read(), ns)
temp, weekend, customers, beta, b_ls = ns["temp"], ns["weekend"], ns["customers"], ns["beta"], ns["b_ls"]
t = np.linspace(-2, 34, 200)
fig, ax = plt.subplots(figsize=(6, 3.8))
for w, color, label in [(0, BLUE, "weekday"), (1, RED, "weekend")]:
    m = weekend == w
    ax.scatter(temp[m], customers[m], s=14, color=color, alpha=0.7, label=label)
    ax.plot(t, np.exp(beta[0] + beta[1] * t + beta[2] * w), color=color, lw=2)
    ax.plot(t, b_ls[0] + b_ls[1] * t + b_ls[2] * w, color=color, lw=1.2, ls="--")
ax.axhline(0, color="black", lw=0.6)
ax.set_xlabel("Temperature (degrees C)")
ax.set_ylabel("Customers, 3 to 4 p.m.")
ax.legend(frameon=False, loc="upper left")
fig.tight_layout()
fig.savefig("smoothie_fit.png", dpi=200)
