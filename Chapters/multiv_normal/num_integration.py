import numpy as np
from scipy.stats import multivariate_normal

# pip3 install scipy
weight_lower_limit = 3.0
weight_upper_limit = 4.0
weight_slices = 100

diameter_lower_limit = 1.5
diameter_upper_limit = 2.0
diameter_slices = 100

# Read the file
data = np.loadtxt("data.txt", delimiter=",", skiprows=1)

# How many snails?
n = data.shape[0]
print(f"n = {n}")

# What's the average weight and diameter
mean_vector = data.mean(axis=0)
print(f"Mean [weight, diameter] = {mean_vector}")

# Do heavier snails tend to have bigger shells?
covariance_matrix = np.cov(data, rowvar=False)
print(f"Covariance = \n{covariance_matrix}")

# Create a multivariate normal distribution
rv = multivariate_normal(mean_vector, covariance_matrix)


delta_weight = (weight_upper_limit - weight_lower_limit) / weight_slices
delta_diameter = (diameter_upper_limit - diameter_lower_limit) / diameter_slices

sum = 0.0
# Step though each different weight
for i in range(weight_slices):
    # What is the weight in the middle of this slice?
    current_weight = weight_lower_limit + (i + 0.5) * delta_weight

    for j in range(diameter_slices):
        # What is the diameter in the middle of this slice?
        current_diameter = diameter_lower_limit + (j + 0.5) * delta_diameter

        # What is the probability density there?
        prob_density = rv.pdf((current_weight, current_diameter))

        # What is the volume under that for this tiny square
        sum += prob_density * delta_weight * delta_diameter

print(
    f"\bThe probability that the weight is between {weight_lower_limit} and {weight_upper_limit}"
)
print(
    f"and that the diameter is between {diameter_lower_limit} and {diameter_upper_limit}"
)
print(f"is about {sum * 100.0:.4f}%")

in_region_count = 0
for i in range(n):
    sample_weight = data[i, 0]
    sample_diameter = data[i, 1]

    if (
        sample_weight >= weight_lower_limit
        and sample_weight <= weight_upper_limit
        and sample_diameter >= diameter_lower_limit
        and sample_diameter <= diameter_upper_limit
    ):
        in_region_count += 1

percent_in_region = in_region_count / n
print(f"{percent_in_region * 100.0:.4f}% of the samples are in the region")
