import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal, norm
# from scipy.stats import gaussian_kde
#pip3 install matplotlib
#pip3 install scipy

# Read the file
data = np.loadtxt("data.txt", delimiter=",", skiprows=1)
n = data.shape[0]

# Basic stats
min_value = 0.0
max_value = max(data[:,0].max(), data[:,1].max()) * 1.05

mean_vector = data.mean(axis=0)
print(f"Mean = {mean_vector}")

covariance_matrix = np.cov(data, rowvar=False)
print(f"Covariance = {covariance_matrix}")

# Plot both variables

fig = plt.figure(figsize=(7,7), dpi=256)
axs = fig.subplots(2,1)
fig.subplots_adjust(hspace=0.3)
axs[0].set_title(f"Button Snails (n={n})")

axs[0].set_xlim(min_value, max_value)
axs[0].set_xlabel("Weight (g)")
axs[0].set_ylabel("Probability Density")

axs[1].set_xlim(min_value, max_value)
axs[1].set_xlabel("Diameter of shell (cm)")
axs[1].set_ylabel("Probability Density")

axs[0].axvline(mean_vector[0], linestyle="dashed" )
axs[1].axvline(mean_vector[1], linestyle="dashed" )

# Standard deviation is the square root of the variance
weight_sd = np.sqrt(covariance_matrix[0,0])
diameter_sd = np.sqrt(covariance_matrix[1,1])
weight_norm = norm(mean_vector[0], weight_sd)
diameter_norm = norm(mean_vector[1], diameter_sd)

axs[0].axvline(mean_vector[0] + weight_sd, lw=0.5)
axs[0].axvline(mean_vector[0] - weight_sd, lw=0.5)

axs[1].axvline(mean_vector[1] + diameter_sd, lw=0.5)
axs[1].axvline(mean_vector[1] - diameter_sd, lw=0.5)

xs = np.linspace(min_value, max_value, 200)
axs[0].plot(xs,weight_norm.pdf(xs),linewidth=0.5,color="black")
axs[1].plot(xs,diameter_norm.pdf(xs),linewidth=0.5,color="black")

zeros = [0] * n;
axs[0].scatter(data[:,0], zeros, marker="+")
axs[1].scatter(data[:,1], zeros, marker="+")

fig.savefig("separate.png")

# Create xyz data
x, y = np.mgrid[min_value:max_value:.01, min_value:max_value:.01]
pos = np.dstack((x, y))

# Create a multivariate normal distribution
rv = multivariate_normal(mean_vector, covariance_matrix)

# Evaluate the PDF at each point in the grid
z = rv.pdf(pos)

# Do a scatter plot with contour lines

fig = plt.figure(figsize=(7,7), dpi=144)
ax = fig.subplots()
ax.set_title(f"Weight and Shell Diameter of Button Snails (n={n})")

ax.set_xlim(min_value, max_value)
ax.set_xlabel("Weight (g)")
ax.set_ylim(min_value, max_value)
ax.set_ylabel("Diameter (cm)")

ax.scatter(data[:,0], data[:,1], marker="+")
fig.savefig("scatter.png")

ax.contour(x,y,z, linewidths=0.5)
ax.axvline(mean_vector[0], lw=0.5, linestyle="dashed")
ax.axhline(mean_vector[1], lw=0.5, linestyle="dashed")

fig.savefig("contour.png")

# Get the figure and axis
fig = plt.figure(figsize=(7,7), dpi=256)
ax = fig.subplots()
ax.set_title(f"Weight and Shell Diameter of Button Snails (n={n})")

ax.set_xlim(min_value, max_value)
ax.set_xlabel("Weight(g)")
ax.set_ylim(min_value, max_value)
ax.set_ylabel("Diameter(cm)")

# Plot the 3D surface
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlabel('PDF')
fig.savefig("3d.png")
