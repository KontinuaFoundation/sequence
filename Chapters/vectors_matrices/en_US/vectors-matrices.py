import numpy as np

A = np.array([[5, 1, 3, -2],
              [1, -1, 8, 4],
              [6, 2, 1, 3]])
b = np.array([1, 2, 3, -8])

print(A.shape)   # (3, 4): 3 rows, 4 columns
print(A @ b)     # [ 32  -9 -11]
print(A.T)       # the 4 x 3 transpose
