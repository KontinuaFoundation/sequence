"""Author tool: draws the figures for this chapter from penguins.csv."""
import numpy as np
import matplotlib.pyplot as plt
from penguins import load_penguins

COLORS = {"Adelie": "#FF8C00", "Chinstrap": "#A034F0", "Gentoo": "#057076"}
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
data = load_penguins()

fig, ax = plt.subplots(figsize=(6, 4))
for name, color in COLORS.items():
    m = data["species"] == name
    ax.scatter(data["flipper_length_mm"][m], data["body_mass_g"][m], s=14, color=color, label=name, alpha=0.8)
ax.set_xlabel("Flipper length (mm)")
ax.set_ylabel("Body mass (g)")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("penguin_regression.png", dpi=200)

fig, ax = plt.subplots(figsize=(6, 4))
markers = {"Adelie": "o", "Chinstrap": "^", "Gentoo": "s"}
for name, color in COLORS.items():
    m = data["species"] == name
    ax.scatter(data["bill_length_mm"][m], data["bill_depth_mm"][m], s=16, color=color, marker=markers[name],
               label=name, alpha=0.8)
ax.set_xlabel("Bill length (mm)")
ax.set_ylabel("Bill depth (mm)")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("penguin_species.png", dpi=200)
