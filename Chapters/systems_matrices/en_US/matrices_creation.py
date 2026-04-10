import numpy as np

A = np.array([[ 5, 1, 3], 
              [ 1, -1, 8], 
              [ 6, 2, 1]])

A.transpose()


B = np.array([[ 5, 1, 6], 
              [ 1, -1, 2], 
              [ 6, 2, 1]])
B.transpose()

J = np.array([[ 5, 1, 3, 0], 
              [ 1, -1, 8, 11], 
              [ 6, 2, 1,-7]])
J.transpose()

# create and 8 by 10 zero matrix
 C = np.zeros((8, 10))
 C
# create an 8 by 8 Identity matrix 
 D = np.eye(8)
 D


W = np.array([[1, 2, 3, 4], 
              [5, 6, 7, 8], 
              [-8, -7, -6, -5],
              [-4, -3, -2, -1]])
print(np.diag(W,0))

Q = np.array([1, 2, 3])
DiagArray = np.diag(Q))
print(DiagArray)
print(np.triu(W))
print(np.tril(W))
