"""Author tool: draws the figures for this chapter."""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
SPECIES = {"Adelie": "#FF8C00", "Chinstrap": "#A034F0", "Gentoo": "#057076"}
CL = ["#005FC6", "#C0392B", "#2E8B57"]
ns = {}
exec(open("kmeans.py").read().split("for k in range(1, 7):")[0], ns)
X, Z, kmeans, data = ns["X"], ns["Z"], ns["kmeans"], ns["data"]

# Clusters versus species
labels, centers, _, _ = min((kmeans(Z, 3, s) for s in range(10)), key=lambda r: r[2])
C = centers * X.std(0) + X.mean(0)
fig, axes = plt.subplots(1, 2, figsize=(9, 3.6), sharey=True)
for j in range(3):
    m = labels == j
    axes[0].scatter(X[m, 0], X[m, 1], s=8, color=CL[j], label=f"cluster {j}")
axes[0].scatter(C[:, 0], C[:, 1], marker="X", s=140, color="black", label="centroid")
axes[0].set_title("k-means clusters (no labels used)", fontsize=11)
for s, c in SPECIES.items():
    m = data["species"] == s
    axes[1].scatter(X[m, 0], X[m, 1], s=8, color=c, label=s)
axes[1].set_title("actual species", fontsize=11)
for ax in axes:
    ax.set_xlabel("Bill length (mm)")
    ax.legend(frameon=False, fontsize=8, loc="lower left")
axes[0].set_ylabel("Bill depth (mm)")
fig.tight_layout()
fig.savefig("clusters.png", dpi=200)

# Elbow plot
ks = range(1, 9)
inert = [min(kmeans(Z, k, s)[2] for s in range(10)) for k in ks]
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(ks, inert, "-o", color="#005FC6")
ax.annotate("elbow", (3, inert[2]), xytext=(4.2, 330), arrowprops=dict(arrowstyle="->"))
ax.set_xlabel("Number of clusters k")
ax.set_ylabel("Total squared distance")
fig.tight_layout()
fig.savefig("elbow.png", dpi=200)

# Iterations from a poor start
centers = Z[[0, 1, 2]].copy()          # three Adelies: a bad start
fig, axes = plt.subplots(1, 4, figsize=(11, 2.9), sharey=True)
for step, ax in enumerate(axes):
    d2 = np.sum((Z[:, None, :] - centers[None, :, :])**2, axis=2)
    lab = d2.argmin(1)
    for j in range(3):
        ax.scatter(Z[lab == j, 0], Z[lab == j, 1], s=5, color=CL[j])
    ax.scatter(centers[:, 0], centers[:, 1], marker="X", s=110, color="black")
    ax.set_title(f"step {step + 1}", fontsize=11)
    ax.set_xlabel("Bill length (std.)")
    centers = np.array([Z[lab == j].mean(0) for j in range(3)])
axes[0].set_ylabel("Bill depth (std.)")
fig.tight_layout()
fig.savefig("steps.png", dpi=200)
