"""Author tool: draws the figures for this chapter."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate2d

# A simple drawing of a house, 64 x 64 pixels
img = np.zeros((64, 64))
img[30:56, 14:50] = 0.6                       # walls
for r in range(12, 30):                       # roof
    half = (r - 12) * 20 // 18
    img[r, 32 - half:32 + half] = 0.9
img[40:56, 28:36] = 0.2                       # door
img[36:44, 18:25] = 1.0                       # windows
img[36:44, 40:47] = 1.0

v = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
fig, axes = plt.subplots(1, 3, figsize=(9, 3.2))
panels = [(img, "image"), (correlate2d(img, v, mode="same"), "vertical-edge filter"),
          (correlate2d(img, v.T, mode="same"), "horizontal-edge filter")]
for ax, (a, title) in zip(axes, panels):
    if title == "image":
        ax.imshow(a, cmap="gray", vmin=0, vmax=1)
    else:
        m = np.abs(a).max()
        ax.imshow(a, cmap="RdBu", vmin=-m, vmax=m)
    ax.set_title(title, fontsize=11)
    ax.set_xticks([])
    ax.set_yticks([])
fig.tight_layout()
fig.savefig("edges.png", dpi=200)
