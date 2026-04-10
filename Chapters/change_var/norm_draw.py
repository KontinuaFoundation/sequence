import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Constants
MEAN = 0.7
STD = 0.08
C = np.power(3 / (4 * np.pi), 1/3)

# Plotting from the 0.5 percentile to the 99.5 percentile
r_min = 0.1
r_max = norm.ppf(0.998, loc=MEAN, scale=STD)

def mass_for_radius(x):
    return 4 * np.pi * (x**3) / 3

def radius_for_mass(x):
    return C * np.power(x, 1/3)

def d_radius_for_mass(x):
    return (C/3) * np.power(x,-2/3)

m_min = mass_for_radius(r_min)
m_max = mass_for_radius(r_max)
m_mean = mass_for_radius(MEAN)

print(f"mean of masses = {m_mean}")
m_minus_std = mass_for_radius(MEAN - STD)
m_plus_std = mass_for_radius(MEAN + STD)
m_minus_2std = mass_for_radius(MEAN - 2 * STD)
m_plus_2std = mass_for_radius(MEAN + 2 * STD)

# Make 200 points between x_min and m_max
r_values = np.linspace(r_min, m_max, 200)

# Get CDF for each x value
cdf_values = norm.cdf(r_values, loc=MEAN, scale=STD)

# Get PDF for each x value
pdf_values = norm.pdf(r_values, loc=MEAN, scale=STD)

# What is the highest density?
max_density = norm.pdf(MEAN, loc=MEAN, scale=STD)

# Make a figure with two axes
fig, axs = plt.subplots(nrows=2, sharex=True, figsize=(10, 7), dpi=200)
axs[0].set_xlim(left=r_min, right=m_max)

# Draw the PDF on the first axis
axs[0].set_title(f"Probability Density of Radius")
axs[0].set_ylim(bottom=0.0, top=max_density * 1.1)
axs[0].set_ylabel("Probability Density")
axs[0].plot(r_values, pdf_values)

# Add lines for mean,  mean-std, and mean+std
axs[0].vlines(MEAN, 0, max_density, "k", linestyle="dashed",lw=0.5)
axs[0].vlines(MEAN - STD, 0, max_density * 0.7, "r", linestyle="dashed",lw=0.5)
axs[0].vlines(MEAN + STD, 0, max_density * 0.7, "r", linestyle="dashed",lw=0.5)
axs[0].vlines(MEAN - 2 * STD, 0, max_density * 0.2, "g", linestyle="dashed",lw=0.5)
axs[0].vlines(MEAN + 2 * STD, 0, max_density * 0.2, "g", linestyle="dashed",lw=0.5)

# Draw the CDF on the second axis
axs[1].set_title("Cumulative Distribution of Radius")
axs[1].set_ylim(bottom=0.0, top=1.0)
axs[1].set_xlabel("radius (cm)")
axs[1].set_ylabel("Probability")
axs[1].plot(r_values, cdf_values)

# Add lines for mean,  mean-std, and mean+std
axs[1].vlines(MEAN, 0, 0.6, "k", linestyle="dashed",lw=0.5)
axs[1].vlines(MEAN - STD, 0, 0.2, "r", linestyle="dashed",lw=0.5)
axs[1].vlines(MEAN + STD, 0, 0.9, "r", linestyle="dashed",lw=0.5)
axs[1].vlines(MEAN - 2 * STD, 0, 0.05, "g", linestyle="dashed",lw=0.5)
axs[1].vlines(MEAN + 2 * STD, 0, 1.0, "g", linestyle="dashed",lw=0.5)

# Save out the figure
fig.savefig("before.png")

m_values = mass_for_radius(r_values)

# Make a figure with two axes
fig, axs = plt.subplots(nrows=2, sharex=True, figsize=(10, 7), dpi=200)

# Draw the CDF on the second axis
axs[0].set_title("Cumulative Distribution")
axs[0].set_ylim(bottom=0.0, top=1.0)
axs[0].set_xlim(left=0.0, right=m_max)
axs[0].set_xlabel("radius (cm)")
axs[0].set_ylabel("Probability")
axs[0].plot(r_values, cdf_values)

# Add lines for mean,  mean-std, and mean+std
axs[0].vlines(MEAN, 0, 0.6, "k", linestyle="dashed",lw=0.5)
axs[0].vlines(MEAN - STD, 0, 0.2, "r", linestyle="dashed",lw=0.5)
axs[0].vlines(MEAN + STD, 0, 0.9, "r", linestyle="dashed",lw=0.5)
axs[0].vlines(MEAN - 2 * STD, 0, 0.05, "g", linestyle="dashed",lw=0.5)
axs[0].vlines(MEAN + 2 * STD, 0, 1.0, "g", linestyle="dashed",lw=0.5)

# Draw the CDF on the second axis
axs[1].set_ylim(bottom=0.0, top=1.0)
axs[1].set_xlim(left=0.0, right=m_max)
axs[1].set_xlabel("mass (g)")
axs[1].set_ylabel("Probability")
axs[1].plot(m_values, cdf_values)

# Add lines for mean,  mean-std, and mean+std
axs[1].vlines(m_mean, 0, 0.6, "k", linestyle="dashed",lw=0.5)
axs[1].vlines(m_plus_std, 0, 0.9, "r", linestyle="dashed",lw=0.5)
axs[1].vlines(m_minus_std, 0, 0.2, "r", linestyle="dashed",lw=0.5)
axs[1].vlines(m_minus_2std, 0, 0.05, "g", linestyle="dashed",lw=0.5)
axs[1].vlines(m_plus_2std, 0, 1.0, "g", linestyle="dashed",lw=0.5)
fig.savefig("cdf_after.png")

m_values = np.linspace(m_min, m_max, 200)
r_values = radius_for_mass(m_values)
cdf_values = norm.cdf(r_values, loc=MEAN, scale=STD)
dg_values = d_radius_for_mass(m_values)

pdf_values = norm.pdf(r_values, loc=MEAN, scale=STD) * dg_values

# Make a figure with two axes
fig, axs = plt.subplots(nrows=2, sharex=True, figsize=(10, 7), dpi=200)

# Draw the CDF on the second axis
axs[0].set_title("CDF of Mass")
axs[0].set_ylim(bottom=0.0, top=1.0)
axs[0].set_xlim(left=0.0, right=m_max)
axs[0].set_ylabel("Probability")
axs[0].plot(m_values, cdf_values)

# Add lines for mean,  mean-std, and mean+std
axs[0].vlines(m_mean, 0, 0.6, "k", linestyle="dashed",lw=0.5)
axs[0].vlines(m_plus_std, 0, 0.9, "r", linestyle="dashed",lw=0.5)
axs[0].vlines(m_minus_std, 0, 0.2, "r", linestyle="dashed",lw=0.5)
axs[0].vlines(m_minus_2std, 0, 0.05, "g", linestyle="dashed",lw=0.5)
axs[0].vlines(m_plus_2std, 0, 1.0, "g", linestyle="dashed",lw=0.5)

# Draw the PDF on the second axis
axs[1].set_title("PDF of Mass")
axs[1].set_ylim(bottom=0.0, top=1.0)
axs[1].set_xlim(left=0.0, right=m_max)
axs[1].set_xlabel("mass (g)")
axs[1].set_ylabel("Probability Density")
axs[1].plot(m_values, pdf_values)

max_density = pdf_values.max()

# Add lines for mean,  mean-std, and mean+std
axs[1].vlines(m_mean, 0, max_density * 1.1, "k", linestyle="dashed",lw=0.5)
axs[1].vlines(m_plus_std, 0, max_density * .65, "r", linestyle="dashed",lw=0.5)
axs[1].vlines(m_minus_std, 0, max_density * .85 , "r", linestyle="dashed",lw=0.5)
axs[1].vlines(m_minus_2std, 0, max_density * .3, "g", linestyle="dashed",lw=0.5)
axs[1].vlines(m_plus_2std, 0, max_density * .2, "g", linestyle="dashed",lw=0.5)
fig.savefig("pdf_after.png")
