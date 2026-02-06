# Our Two Main Libraries, NumPy and Matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Transformation matrix (YOUR INPUT TRANSFORMATION MATRIX HERE)
# UNCOMMENT ONE OF THE FOLLOWING OPTIONS

# Identity matrix (no transformation)
# A = np.array([[1, 0],
#               [0, 1]])
# current_transform = "identity"
# Scaled both basis vectors by factor 2
A = np.array([[2, 0],
              [0, 2]])
current_transform = "scaling_2x"

# Scaled along y-axis by factor 2
# A = np.array([[1, 0],
#               [0, 2]])
# current_transform = "scaling_y2x"
# Reflection about y axis
# A = np.array([[-1, 0],
#               [0, 1]])
# current_transform = "reflection_y_axis"
# Reflection about x axis
# A = np.array([[1, 0],
#               [0, -1]])
# current_transform = "reflection_x_axis"
# Reflection across line y=x
# A = np.array([[0, 1],
#               [1, 0]])
# current_transform = "reflection_y_eq_x"
# Reflection across line y=-x
# A = np.array([[0, -1],
#               [-1, 0]])
# current_transform = "reflection_y_eq_neg_x"
# ----------- ROTATIONS --------
# 90 degree rotation clockwise
# A = np.array([[0, 1],
#               [-1, 0]])
# current_transform = "rotation_90deg_cw"
# 90 degree rotation ccw
# A = np.array([[0, -1],
#               [1, 0]])
# current_transform = "rotation_90deg_ccw"
# theta definition in degrees

theta = np.deg2rad(30)  # Change 30 to any angle you want in degrees

# theta degree rotation clockwise
# A = np.array([[np.cos(theta), np.sin(theta)],
#               [-np.sin(theta), np.cos(theta)]])

# theta degree rotation ccw
# A = np.array([[np.cos(theta), -np.sin(theta)],
#               [np.sin(theta), np.cos(theta)]])

# Create a grid of points
num_points = 10
x_grid = np.linspace(-2, 2, num_points) # 10 evenly spaced points from -2 to 2
y_grid = np.linspace(-2, 2, num_points) # 10 evenly spaced points from -2 to 2

# The grid points as column vectors (the vectors to be transformed)
# A is 2x2 so we need 2xN input vectors
# then we transpose at the end to get the right shape of 2xN
X = np.array([[i, j] for i in x_grid for j in y_grid]).T  

# Apply transformation
B = A @ X

# Plot
plt.figure()
plt.scatter(X[0], X[1], s=10, color="#868BCF", label="x (input)")
plt.scatter(B[0], B[1], s=10, color="#08446c", label="Ax (output)")
# Standard basis vectors
E = np.eye(2)      # e1, e2
AE = A @ E         # A e1, A e2

# for when basis vectors overlap
offset = 0.025
# Basis - Before (standard basis)
plt.quiver([0, 0], [0, 0], E[0], E[1],
           angles="xy", scale_units="xy", scale=1,
           color="green",linestyle="--")

# After (transformed basis)
plt.quiver([offset, offset], [offset, offset], AE[0], AE[1],
           angles="xy", scale_units="xy", scale=1,
           color="#0D533F",)
x = np.linspace(-2, 2, 100)

# Plot lines y=x and y=-x for reference for reflections
# plt.plot(x, -x)


# Test vector for visualization : [1, 1]
V = np.array([2, 2])
AV = A @ V
plt.quiver([0, 0], [0, 0], V[0], V[1],
           angles="xy", scale_units="xy", scale=1,
           color="#E516DB", linestyle="--")
plt.quiver([offset, offset], [offset, offset], AV[0], AV[1],
           angles="xy", scale_units="xy", scale=1,
           color="#82037C")

plt.axis("equal")
plt.axhline(0, linestyle="--", linewidth=0.8, alpha=0.7)
plt.axvline(0, linestyle="--", linewidth=0.8, alpha=0.7)

legend_elements = [
    Line2D([0], [0], marker='o', linestyle='',
           color="#868BCF", label="x (input)"),
    Line2D([0], [0], marker='o', linestyle='',
           color="#08446c", label="Ax (output)"),
    Line2D([0], [0], color="green", linewidth=2,
           label="basis vectors"),
    Line2D([0], [0], color="#0D533F", linewidth=2,
           label="transformed basis vectors"),
    Line2D([0], [0], color="#E516DB", linewidth=2,
           label="test vector v"),
    Line2D([0], [0], color="#82037C", linewidth=2,
           label="transformed test vector Av"),
]

plt.legend(handles=legend_elements, loc="upper left", fontsize="small")
plt.savefig(f"grid_{current_transform}.png")
plt.show()
