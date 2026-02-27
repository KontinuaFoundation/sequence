from scipy.stats import norm

# Given parameters
mu = 75
sigma = 8

# Calculate the probability that a randomly selected student scored between 80 and 90
probability = norm.cdf(90, loc=mu, scale=sigma) - norm.cdf(80, loc=mu, scale=sigma)
print(f"The probability that a randomly selected student scored between 80 and 90 is: {probability:.4f}")
