import numpy as np
from penguins import load_penguins

data = load_penguins()
X = np.column_stack([data["bill_length_mm"], data["bill_depth_mm"]])
Z = (X - X.mean(axis=0)) / X.std(axis=0)            # standardize first

def kmeans_plus_plus(Z, k, rng):
    """Spread out the starting centroids: each new one is chosen with
    probability proportional to its squared distance from the nearest so far."""
    centers = [Z[rng.integers(len(Z))]]
    for _ in range(k - 1):
        d2 = np.min([np.sum((Z - c)**2, axis=1) for c in centers], axis=0)
        centers.append(Z[rng.choice(len(Z), p=d2 / d2.sum())])
    return np.array(centers)

def kmeans(Z, k, seed=0, max_steps=100):
    rng = np.random.default_rng(seed)
    centers = kmeans_plus_plus(Z, k, rng)
    for step in range(max_steps):
        # Assign: squared distance from every point to every center
        d2 = np.sum((Z[:, None, :] - centers[None, :, :])**2, axis=2)
        labels = d2.argmin(axis=1)
        # Update: move each center to the mean of its points
        new = np.array([Z[labels == j].mean(axis=0) for j in range(k)])
        if np.allclose(new, centers):
            break
        centers = new
    inertia = np.sum((Z - centers[labels])**2)        # total squared distance
    return labels, centers, inertia, step + 1

for k in range(1, 7):
    best = min((kmeans(Z, k, seed) for seed in range(10)), key=lambda r: r[2])
    print(f"k = {k}: total squared distance {best[2]:6.1f}")

labels, centers, inertia, steps = min((kmeans(Z, 3, seed) for seed in range(10)),
                                      key=lambda r: r[2])
print(f"k = 3 converged in {steps} steps")
print("Centers in mm:")
print(np.round(centers * X.std(axis=0) + X.mean(axis=0), 1))

species = data["species"]
print("cluster  Adelie  Chinstrap  Gentoo")
for j in range(3):
    counts = [np.sum((labels == j) & (species == s)) for s in ("Adelie", "Chinstrap", "Gentoo")]
    print(f"{j:7d} {counts[0]:7d} {counts[1]:10d} {counts[2]:7d}")
