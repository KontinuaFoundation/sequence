"""Author tool: draws the figures for this chapter."""
import csv
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from scipy import stats
from penguins import load_penguins
from text import prepare

plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
COLORS = ["#FF8C00", "#A034F0", "#057076"]
BLUE, RED = "#005FC6", "#C0392B"

# Spammiest and hammiest words
rows = list(csv.DictReader(open("messages.csv", newline="")))
counts = {"spam": Counter(), "ham": Counter()}
for r in rows:
    counts[r["label"]].update(prepare(r["text"]))
vocab = sorted(set(counts["spam"]) | set(counts["ham"]))
ts, th = sum(counts["spam"].values()), sum(counts["ham"].values())
ratio = {w: np.log((counts["spam"][w] + 1) / (ts + len(vocab))) - np.log((counts["ham"][w] + 1) / (th + len(vocab)))
         for w in vocab}
ranked = sorted(vocab, key=lambda w: ratio[w])
show = ranked[:8] + ranked[-8:]
fig, ax = plt.subplots(figsize=(6, 4))
vals = [ratio[w] for w in show]
ax.barh(range(len(show)), vals, color=[RED if v > 0 else BLUE for v in vals])
ax.set_yticks(range(len(show)), show)
ax.axvline(0, color="black", lw=0.8)
ax.set_xlabel(r"$\ln P(\mathrm{word} \mid \mathrm{spam}) - \ln P(\mathrm{word} \mid \mathrm{ham})$")
fig.tight_layout()
fig.savefig("spam_words.png", dpi=200)

# Naive versus full Gaussian densities for penguins
data = load_penguins()
names, y = np.unique(data["species"], return_inverse=True)
F = np.column_stack([data["bill_length_mm"], data["bill_depth_mm"]])
order = np.random.default_rng(1).permutation(len(y))
dev = order[:266]
gx, gy = np.meshgrid(np.linspace(32, 60, 300), np.linspace(12.5, 22, 300))
grid = np.dstack([gx, gy])
fig, axes = plt.subplots(1, 2, figsize=(9, 3.8), sharey=True)
for ax, naive in zip(axes, [True, False]):
    for c in range(3):
        g = F[dev][y[dev] == c]
        cov = np.cov(g.T, bias=True)
        if naive:
            cov = np.diag(np.diag(cov))
        dens = stats.multivariate_normal(g.mean(0), cov).pdf(grid)
        peak = dens.max()
        ax.contour(gx, gy, dens, levels=[peak * 0.1, peak * 0.4, peak * 0.8], colors=COLORS[c], linewidths=1)
        ax.scatter(g[:, 0], g[:, 1], s=6, color=COLORS[c], alpha=0.5, label=names[c])
    ax.plot(45, 17, "*", color="black", ms=12)
    ax.set_title("naive (independent)" if naive else "full covariance", fontsize=11)
    ax.set_xlabel("Bill length (mm)")
axes[0].set_ylabel("Bill depth (mm)")
axes[1].legend(frameon=False, fontsize=8, loc="lower right")
fig.tight_layout()
fig.savefig("gaussians.png", dpi=200)
