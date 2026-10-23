"""Author tool: draws the figures for this chapter."""
import numpy as np
import matplotlib.pyplot as plt
from penguins import load_penguins

plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
BLUE, RED, GRAY, PURPLE = "#005FC6", "#C0392B", "#9a9a9a", "#A034F0"

data = load_penguins()
y = (data["species"] == "Chinstrap").astype(int)
F = np.column_stack([data["bill_length_mm"], data["bill_depth_mm"]])
n = len(y)
order = np.random.default_rng(1).permutation(n)
train, test = order[:233], order[233:]
X = np.column_stack([np.ones(n), (F - F[train].mean(0)) / F[train].std(0)])
sigmoid = lambda z: 1 / (1 + np.exp(-z))
theta = np.zeros(3)
for _ in range(3000):
    theta -= 0.5 * X[train].T @ (sigmoid(X[train] @ theta) - y[train]) / len(train)
scores, actual = sigmoid(X[test] @ theta), y[test]

# Scores by class
bins = np.linspace(0, 1, 21)
fig, ax = plt.subplots(figsize=(6, 3))
ax.hist(scores[actual == 0], bins=bins, color=GRAY, label="not Chinstrap (74)")
ax.hist(scores[actual == 1], bins=bins, color=PURPLE, alpha=0.8, label="Chinstrap (26)")
ax.axvline(0.5, color="black", ls="--", lw=1.2)
ax.text(0.52, 10.5, "threshold 0.5", fontsize=9)
ax.set_ylim(0, 12)
counts, _ = np.histogram(scores[actual == 0], bins=bins)
for k in np.nonzero(counts > 12)[0]:
    ax.text(bins[k] + 0.025, 11, str(counts[k]), fontsize=8, color="white", ha="center")
ax.set_xlabel("Predicted P(Chinstrap)")
ax.set_ylabel("Test penguins")
ax.legend(frameon=False, fontsize=9, loc="upper right")
fig.tight_layout()
fig.savefig("scores.png", dpi=200)

# ROC and precision-recall curves
ranked = actual[np.argsort(-scores)]
tpr = np.concatenate([[0], np.cumsum(ranked) / ranked.sum()])
fpr = np.concatenate([[0], np.cumsum(1 - ranked) / (1 - ranked).sum()])
tp = np.cumsum(ranked)
precision = tp / np.arange(1, n - 233 + 1)
recall = tp / ranked.sum()
fig, axes = plt.subplots(1, 2, figsize=(8, 3.6))
ax = axes[0]
ax.plot(fpr, tpr, color=BLUE, lw=2)
ax.fill_between(fpr, tpr, step=None, color=BLUE, alpha=0.1)
ax.plot([0, 1], [0, 1], color=GRAY, ls="--", lw=1)
for th in [0.1, 0.3, 0.5, 0.7]:
    pred = scores >= th
    x_ = np.sum(pred & (actual == 0)) / 74
    y_ = np.sum(pred & (actual == 1)) / 26
    ax.plot(x_, y_, "o", color=RED, ms=5)
    ax.annotate(f"{th}", (x_, y_), xytext=(6, -10), textcoords="offset points", fontsize=9, color=RED)
ax.text(0.45, 0.3, "AUC = 0.921", color=BLUE)
ax.set_xlabel("False positive rate")
ax.set_ylabel("True positive rate (recall)")
ax.set_title("ROC curve", fontsize=11)
ax.set_aspect("equal")
ax = axes[1]
ax.plot(recall, precision, color=BLUE, lw=2)
ax.axhline(26 / 100, color=GRAY, ls="--", lw=1)
ax.text(0.02, 0.29, "always say Chinstrap", fontsize=9, color=GRAY)
ax.set_xlabel("Recall")
ax.set_ylabel("Precision")
ax.set_ylim(0, 1.05)
ax.set_title("Precision-recall curve", fontsize=11)
fig.tight_layout()
fig.savefig("roc_pr.png", dpi=200)
