"""Author tool: draws the figures for this chapter."""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
BLUE, RED, GRAY = "#005FC6", "#C0392B", "#9a9a9a"

# AdaBoost accuracy against rounds
ns = {}
exec(open("adaboost.py").read().split("w = np.full")[0], ns)
X, y, train, test = ns["X"], ns["y"], ns["train"], ns["test"]
best_stump, stump_predict = ns["best_stump"], ns["stump_predict"]
w = np.full(len(train), 1 / len(train))
st, ss = np.zeros(len(train)), np.zeros(len(test))
acc_tr, acc_te = [], []
for t in range(200):
    s = best_stump(X[train], y[train], w)
    a = 0.5 * np.log((1 - s[0]) / s[0])
    h = stump_predict(s, X[train])
    w = w * np.exp(-a * y[train] * h)
    w /= w.sum()
    st += a * h
    ss += a * stump_predict(s, X[test])
    acc_tr.append(np.mean(np.sign(st) == y[train]))
    acc_te.append(np.mean(np.sign(ss) == y[test]))
fig, ax = plt.subplots(figsize=(5.5, 3))
ax.plot(range(1, 201), acc_tr, color=BLUE, lw=1.8, label="training")
ax.plot(range(1, 201), acc_te, color=RED, lw=1.8, label="test")
ax.set_xlabel("Number of stumps")
ax.set_ylabel("Accuracy")
ax.legend(frameon=False, loc="lower right")
fig.tight_layout()
fig.savefig("adaboost_curve.png", dpi=200)

# Gradient boosting on flipper length alone: the fit after a few rounds
ns = {}
exec(open("gradient_boost.py").read().split("rate = 0.1")[0], ns)
data, y, train, fit_stump, stump_predict = ns["data"], ns["y"], ns["train"], ns["fit_stump"], ns["stump_predict"]
f = data["flipper_length_mm"][:, None]
xs = np.linspace(170, 232, 500)[:, None]
pred = np.full(len(train), y[train].mean())
curve = np.full(len(xs), y[train].mean())
fig, axes = plt.subplots(1, 3, figsize=(10, 3.2), sharey=True)
shown = {1: axes[0], 10: axes[1], 100: axes[2]}
for t in range(1, 101):
    s = fit_stump(f[train], y[train] - pred)
    pred += 0.1 * stump_predict(s, f[train])
    curve += 0.1 * stump_predict(s, xs)
    if t in shown:
        ax = shown[t]
        ax.scatter(f[train, 0], y[train], s=6, color=GRAY)
        ax.plot(xs[:, 0], curve, color=RED, lw=2)
        ax.set_title(f"after {t} stump" + ("s" if t > 1 else ""), fontsize=11)
        ax.set_xlabel("Flipper length (mm)")
axes[0].set_ylabel("Body mass (g)")
fig.tight_layout()
fig.savefig("boost_steps.png", dpi=200)

# Gradient boosting RMSE against rounds
X, test = ns["X"], ns["test"]
p_tr = np.full(len(train), y[train].mean())
p_te = np.full(len(test), y[train].mean())
r_tr, r_te = [], []
for t in range(500):
    s = fit_stump(X[train], y[train] - p_tr)
    p_tr += 0.1 * stump_predict(s, X[train])
    p_te += 0.1 * stump_predict(s, X[test])
    r_tr.append(np.sqrt(np.mean((y[train] - p_tr)**2)))
    r_te.append(np.sqrt(np.mean((y[test] - p_te)**2)))
fig, ax = plt.subplots(figsize=(5.5, 3))
ax.plot(range(1, 501), r_tr, color=BLUE, lw=1.8, label="training")
ax.plot(range(1, 501), r_te, color=RED, lw=1.8, label="test")
ax.axhline(278, color=GRAY, ls="--", lw=1)
ax.text(300, 283, "least squares, test", color="#555555", fontsize=9)
ax.set_ylim(220, 500)
ax.set_xlabel("Number of stumps")
ax.set_ylabel("RMSE (g)")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("gb_curve.png", dpi=200)
