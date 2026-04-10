import numpy as np
import pickle
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

# Ranges for length and weight
xlims = (7.0, 23.0)
ylims = (0.2, 4.4)

# Read the data
with open("data.pkl", "rb") as f:
    fish_dict = pickle.load(f)

# What are their names?
fish_names = list(fish_dict.keys())

# Some colors
colors = ["red", "green", "blue"]

# Prepare the data for plotting
n = 0
fish_colors = {}
fish_data = {}
fish_mu = {}
fish_cov = {}
for i, fish_name in enumerate(fish_names):

    # Convert to a numpy array
    a = np.array(fish_dict[fish_name])
    fish_data[fish_name] = a

    # Sum up the total fish
    n += a.shape[0]

    # Get the mean
    fish_mu[fish_name] = a.mean(axis=0)

    # Here is where we use the variance of each variable
    # independently instead of the covariance
    fish_cov[fish_name] = np.diag(a.var(axis=0))

    # Make a color for each breed of fish
    color_tuple = colors[i]
    fish_colors[fish_name] = color_tuple

# Make the plot
fig, axis = plt.subplots(figsize=(10, 10))
axis.set_title(f"Fish We Measured (n={n})")
axis.set_xlabel("length (cm)")
axis.set_ylabel("weight (kg)")
axis.set_xlim(xlims)
axis.set_ylim(ylims)

# Levels
levels = [0.01 * x for x in range(8)]

# Loop for each breed we have data for
for fish_name in fish_names:

    # Get the array with the data
    a = fish_data[fish_name]
    count = a.shape[0]

    # What color for this breed?
    c = fish_colors[fish_name]

    # Scatter plot!
    axis.scatter(
        a[:, 0], a[:, 1], label=f"{fish_name} (n={count})", color=c, marker="+"
    )

    # Get stats for multivariate normal
    mu = fish_mu[fish_name]
    cov = fish_cov[fish_name]

    # Compute the prior
    p = count / n

    # Make contour plot
    x, y = np.mgrid[xlims[0] : xlims[1] : 0.1, ylims[0] : ylims[1] : 0.1]
    rv = multivariate_normal(mu, cov)
    data = np.dstack((x, y))
    z = rv.pdf(data) * p
    axis.contour(x, y, z, levels, colors=c, alpha=0.5)

# Add a legend to the plot
axis.legend()
fig.savefig("4_indep_density.png")
plt.show()
