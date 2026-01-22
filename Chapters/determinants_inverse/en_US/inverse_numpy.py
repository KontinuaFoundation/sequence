import numpy as np

A = np.array([[2, 1],
              [3, 2]], dtype=float)

# BAD PRACTICE:
# A_inv = np.linalg.inv(A)
# print(A_inv)

detA = np.linalg.det(A)

tolerance = 1e-12  

if abs(detA) < tolerance: 
    print("Matrix is singular or nearly singular. No reliable inverse.")
else:
    A_inv = np.linalg.inv(A)
    print("Determinant:", detA)
    print("Inverse:\n", A_inv)