import numpy as np

A = np.array([[5, 4],
              [1, 2]])
values, vectors = np.linalg.eig(A)

print("Eigenvalues:", values)
print("Eigenvectors (one per column):")
print(vectors)

# Check the first pair: A v should equal lambda v
v = vectors[:, 0]
print(A @ v, values[0] * v)
