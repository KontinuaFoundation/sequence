import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["savefig.directory"] = "" # save image into current directory

def make_grid(x_size=5, y_size=5, num_points=21):
    """Create a grid of points.
        returns a 2xN array of points.
    """
    x = np.linspace(-x_size, x_size, num_points)
    y = np.linspace(-y_size, y_size, num_points)
    X, Y = np.meshgrid(x, y)
    points = np.vstack([X.ravel(), Y.ravel()])
    return points

def make_house():
    """Create the vertices of a simple house shape."""
    house = np.array([[ -1,  -1],
                      [  1,  -1],
                      [  1,   1],
                      [  0,   2],
                      [ -1,   1],
                      [ -1,  -1],
                      [-0.7,  -1],
                      [-0.7,  -0.3],
                      [-0.3,  -0.3],
                      [-0.3,  -1],
                      [ -1,  -1],
                      [ -1,   1],
                      [  1,   1],
                      [0.5, 1.5], # chimney
                      [0.5, 1.8],
                      [0.8, 1.8],
                      [0.8, 1.2]]).T
    return house
grid  = make_grid(3,3,13) 
house = make_house()
# Identity MATRIX
# A = np.array([[1, 0],
#               [0, 1]])
# current_transform = "identity"

# 2x SCALING MATRIX
# A = np.array([[2, 0],
#               [0, 2]])
# current_transform = "scaling_2x"
# 1/2 SCALING MATRIX
# A = np.array([[0.5, 0],
#               [0, 0.5]])
# current_transform = "scaling_0.5x"
# LINEAR RIGHTWARD SHEAR MATRIX (only y component scaled)
# k=2.0
# A = np.array([[1, k],
#               [0, 1]])
# current_transform = f"shear_k{k}"

# REFLECTION ACROSS X-AXIS
# A = np.array([[1, 0],
#               [0, -1]])
# current_transform = "reflection_x_axis"
# REFLECTION ACROSS Y-AXIS
# A = np.array([[-1, 0],
#               [0, 1]])
# current_transform = "reflection_y_axis"
# REFLECTION ACROSS y=x
# A = np.array([[0, 1],
#               [1, 0]])
# current_transform = "reflection_y_equals_x_axis"
# REFLECTION ACROSS y=-x
# A = np.array([[0, -1],
#               [-1, 0]])
# current_transform = "reflection_y_equals_neg_x_axis"

# LINEAR ROTATION (CW) MATRIX
# theta = np.radians(30) # 30 degrees
# A = np.array([[np.cos(theta), np.sin(theta)],
#               [-np.sin(theta),  np.cos(theta)]])
# current_transform = f"rotation_cw_{int(np.degrees(theta))}deg"
# LINEAR ROTATION (CCW) MATRIX
theta = np.radians(30) # 30 degrees
A = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
current_transform = f"rotation_ccw_{int(np.degrees(theta))}deg"
house_sheared = A @ house
grid_sheared  = A @ grid

plt.scatter(grid[0, :], grid[1, :], s=5)
plt.plot(house[0, :], house[1, :], color='black', linewidth=2)

plt.scatter(grid_sheared[0, :], grid_sheared[1, :], s=5)
plt.plot(house_sheared[0, :], house_sheared[1, :], color='red', linewidth=2)

plt.axis('equal')
plt.savefig(f"house_{current_transform}.png")
plt.show()



 # Rotation:
# A = [[cosθ, -sinθ],
#      [sinθ,  cosθ]]

# Shear:
# A = [[1, k],
#      [0, 1]]