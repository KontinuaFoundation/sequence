# import numpy as np
# import matplotlib.pyplot as plt

# A = np.array([[2, 1],
#               [1, 1]])

# v = np.array([1, 2])

# v_transformed = A @ v
# print(v_transformed)


# origin = np.array([[0, 0]])

# plt.quiver(*origin.T, v[0], v[1],
#            angles='xy', scale_units='xy', scale=1,
#            color='blue', label='Original vector')

# plt.quiver(*origin.T, v_transformed[0], v_transformed[1],
#            angles='xy', scale_units='xy', scale=1,
#            color='red', label='Transformed vector')

# plt.xlim(-5, 5)
# plt.ylim(-5, 5)
# plt.axhline(0, color='black')
# plt.axvline(0, color='black')
# plt.grid()
# plt.legend()
# plt.gca().set_aspect('equal')

# plt.show()

# # Create a grid of points
# x = np.linspace(-2, 2, 10)
# y = np.linspace(-2, 2, 10)
# X, Y = np.meshgrid(x, y)

# points = np.vstack([X.ravel(), Y.ravel()])

# # Apply transformation
# transformed_points = A @ points

# plt.figure(figsize=(6, 6))

# # Original grid
# plt.scatter(points[0], points[1], color='blue', alpha=0.5, label='Original')

# # Transformed grid
# plt.scatter(transformed_points[0], transformed_points[1],
#             color='red', alpha=0.5, label='Transformed')

# plt.axhline(0, color='black')
# plt.axvline(0, color='black')
# plt.grid()
# plt.legend()
# plt.gca().set_aspect('equal')
# # plt.show()



# show sheared grid
# import numpy as np
# import matplotlib.pyplot as plt

# # Shear factor
# k = 1.0

# A = np.array([[1, k],
#               [0, 1]])

# # Create grid
# x = np.linspace(-2, 2, 10)
# y = np.linspace(-2, 2, 10)
# X, Y = np.meshgrid(x, y)
# points = np.vstack([X.ravel(), Y.ravel()])

# # Apply shear
# sheared = A @ points
# for i in range(X.shape[0]):
#     # Horizontal lines
#     row = np.vstack([X[i], Y[i]])
#     sheared_row = A @ row
#     plt.plot(row[0], row[1], color='blue', alpha=0.4)
#     plt.plot(sheared_row[0], sheared_row[1], color='red')

# for j in range(X.shape[1]):
#     # Vertical lines
#     col = np.vstack([X[:, j], Y[:, j]])
#     sheared_col = A @ col
#     plt.plot(col[0], col[1], color='blue', alpha=0.4)
#     plt.plot(sheared_col[0], sheared_col[1], color='red')


# plt.axhline(0, color='black')
# plt.axvline(0, color='black')
# plt.grid()
# plt.legend()
# plt.gca().set_aspect('equal')
# plt.show()


