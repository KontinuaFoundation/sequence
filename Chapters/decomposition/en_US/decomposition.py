import numpy as np

A = np.array([[1, 2],
              [3, 4],
              [5, 6]])

U, S, VT = np.linalg.svd(A)
print("U (left singular vectors):")
print(U)
print("Singular values:", S)
print("V transpose (right singular vectors):")
print(VT)

# Rebuild A. Sigma must be the same shape as A (3 x 2).
Sigma = np.zeros(A.shape)
Sigma[:2, :2] = np.diag(S)
print("Rebuilt A:")
print(U @ Sigma @ VT)
