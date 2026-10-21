import numpy as np
from scipy.linalg import sqrtm
import cvxpy as cp     # a module for solving optimization problems

edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
n = 5

# X is the matrix of dot products x_i . x_j; it must be positive semidefinite
X = cp.Variable((n, n), symmetric=True)
constraints = [X >> 0]
# Unit vectors: each x_i . x_i = 1
constraints += [X[i, i] == 1 for i in range(n)]

objective = sum(0.5 * (1 - X[i, j]) for (i, j) in edges)
prob = cp.Problem(cp.Maximize(objective), constraints)
print("Relaxed value:", round(prob.solve(), 3))

# Recover the vectors: the rows of the square root of X
vectors = np.real(sqrtm(X.value))

# Round: slice the sphere with a random plane through the origin
rng = np.random.default_rng(1)
normal = rng.standard_normal(n)
side = np.sign(vectors @ normal)
print("Sides:", side)

cut = sum(1 for (i, j) in edges if side[i] != side[j])
print("Edges cut:", cut)
