import numpy as np
import matplotlib.pyplot as plt


# SCALING X COMPONENT
A = np.array([[2, 0],
              [0, 1]])

# Standard basis vectors and (1,1)
e1 = np.array([1, 0])
e2 = np.array([0, 1])
x  = np.array([1, 1])

Ae1 = A @ e1
Ae2 = A @ e2
Ax  = A @ x

origin = np.array([[0, 0]])

plt.figure()

# Plot vectors
plt.quiver(*origin.T, Ae1[0], Ae1[1], angles='xy', scale_units='xy', scale=1)
plt.quiver(*origin.T, Ae2[0], Ae2[1], angles='xy', scale_units='xy', scale=1)
plt.quiver(*origin.T, Ax[0],  Ax[1],  angles='xy', scale_units='xy', scale=1)

# Axes and formatting
plt.axhline(0)
plt.axvline(0)
# Major grid (integer lattice)
plt.xticks(np.arange(-1, 5, 1))
plt.yticks(np.arange(-1, 5, 1))
plt.grid(True)

# Minor grid (optional, for perspective)
plt.minorticks_on()
plt.grid(which='minor', linewidth=0.5)

plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(-0.5, 1.5)
plt.ylim(-0.5, 1.5)

plt.title("Standard Basis Vectors and [1,1]")
plt.show()
