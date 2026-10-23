"""Author tool: draws the figures for this chapter."""
import copy
import numpy as np
import torch
from torch import nn
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
BLUE, RED, GRAY = "#005FC6", "#C0392B", "#9a9a9a"

# Temperature fits with different numbers of hidden neurons
rng = np.random.default_rng(0)
hours = np.arange(0, 24, 0.25)
temps = 12 - 6 * np.cos(2 * np.pi * (hours - 3) / 24) + rng.normal(0, 0.8, len(hours))
mean, sd = temps.mean(), temps.std()
x = torch.tensor((hours - 12) / 12, dtype=torch.float32).unsqueeze(1)
y = torch.tensor((temps - mean) / sd, dtype=torch.float32).unsqueeze(1)
grid = torch.linspace(-1, 1, 400).unsqueeze(1)
fig, axes = plt.subplots(1, 3, figsize=(10, 3), sharey=True)
def fit(h, seed):
    torch.manual_seed(seed)
    model = nn.Sequential(nn.Linear(1, h), nn.ReLU(), nn.Linear(h, 1))
    opt = torch.optim.Adam(model.parameters(), lr=0.01)
    for _ in range(2000):
        opt.zero_grad()
        loss = nn.functional.mse_loss(model(x), y)
        loss.backward()
        opt.step()
    return loss.item(), model

for ax, h in zip(axes, [2, 4, 16]):
    _, model = min((fit(h, s) for s in range(5)), key=lambda r: r[0])   # best of 5 starts
    with torch.no_grad():
        curve = model(grid).squeeze().numpy() * sd + mean
    ax.scatter(hours, temps, s=6, color=GRAY)
    ax.plot(grid.squeeze().numpy() * 12 + 12, curve, color=RED, lw=2)
    ax.set_title(f"{h} hidden neuron" + ("s" if h > 1 else ""), fontsize=11)
    ax.set_xlabel("Hour of the day")
    ax.set_xticks([0, 6, 12, 18, 24])
axes[0].set_ylabel("Temperature (degrees C)")
fig.tight_layout()
fig.savefig("temperature_fits.png", dpi=200)

# Training and validation curves for the penguin network
ns = {}
src = open("penguin_net.py").read().split("best_val, best_state")[0]
exec(src, ns)
model, optimizer, loss_fn = ns["model"], ns["optimizer"], ns["loss_fn"]
x_tr, y_tr, x_va, y_va, y_sd = ns["x_tr"], ns["y_tr"], ns["x_va"], ns["y_va"], ns["y_sd"]
tr, va = [], []
for epoch in range(1000):
    optimizer.zero_grad()
    loss = loss_fn(model(x_tr), y_tr)
    loss.backward()
    optimizer.step()
    tr.append(ns["rmse_grams"](x_tr, y_tr))
    va.append(ns["rmse_grams"](x_va, y_va))
best = int(np.argmin(va)) + 1
fig, ax = plt.subplots(figsize=(5.8, 3.2))
ax.plot(range(1, 1001), tr, color=BLUE, lw=1.8, label="training")
ax.plot(range(1, 1001), va, color=RED, lw=1.8, label="validation")
ax.axvline(best, color=GRAY, ls="--", lw=1)
ax.text(best + 15, 520, f"best validation\n(epoch {best})", fontsize=9, color="#555555")
ax.set_ylim(100, 700)
ax.set_xlabel("Epoch")
ax.set_ylabel("RMSE (g)")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("penguin_curves.png", dpi=200)
