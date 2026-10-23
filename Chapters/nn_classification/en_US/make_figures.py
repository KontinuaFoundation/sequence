"""Author tool: draws the figures for this chapter."""
import numpy as np
import torch
from torch import nn
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from penguins import load_penguins

plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
COLORS = ["#FF8C00", "#A034F0", "#057076"]

data = load_penguins()
names, labels = np.unique(data["species"], return_inverse=True)
X = np.column_stack([data["bill_length_mm"], data["bill_depth_mm"]])
mean, sd = X.mean(0), X.std(0)
x = torch.tensor((X - mean) / sd, dtype=torch.float32)
y = torch.tensor(labels)
gx, gy = np.meshgrid(np.linspace(31, 61, 300), np.linspace(12.5, 22, 300))
grid = torch.tensor((np.column_stack([gx.ravel(), gy.ravel()]) - mean) / sd, dtype=torch.float32)

fig, axes = plt.subplots(1, 2, figsize=(9, 3.6), sharey=True)
for ax, hidden, title in [(axes[0], None, "no hidden layer (softmax regression)"),
                          (axes[1], 32, "two hidden layers of 32 ReLUs")]:
    torch.manual_seed(0)
    if hidden is None:
        model = nn.Linear(2, 3)
    else:
        model = nn.Sequential(nn.Linear(2, hidden), nn.ReLU(), nn.Linear(hidden, hidden), nn.ReLU(),
                              nn.Linear(hidden, 3))
    opt = torch.optim.Adam(model.parameters(), lr=0.01)
    for _ in range(1500):
        opt.zero_grad()
        loss = nn.functional.cross_entropy(model(x), y)
        loss.backward()
        opt.step()
    with torch.no_grad():
        regions = model(grid).argmax(1).numpy().reshape(gx.shape)
        acc = (model(x).argmax(1) == y).float().mean().item()
    ax.contourf(gx, gy, regions, levels=[-0.5, 0.5, 1.5, 2.5], cmap=ListedColormap(COLORS), alpha=0.25)
    for c in range(3):
        m = labels == c
        ax.scatter(X[m, 0], X[m, 1], s=7, color=COLORS[c], label=names[c])
    ax.set_title(f"{title}\ntraining accuracy {acc:.1%}", fontsize=10)
    ax.set_xlabel("Bill length (mm)")
axes[0].set_ylabel("Bill depth (mm)")
axes[1].legend(frameon=False, fontsize=8, loc="lower right")
fig.tight_layout()
fig.savefig("nn_regions.png", dpi=200)
