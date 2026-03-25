
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Data
experience = [3, 8, 1, 0, 5, 10, 2, 7, 4, 6]
salary     = [36, 43, 32, 30, 38, 47, 33, 42, 37, 41]

# Least-squares regression
slope, intercept, r, p, se = stats.linregress(experience, salary)

print(f"Slope (b):     {slope:.3f}")
print(f"Intercept (a): {intercept:.3f}")
print(f"r:             {r:.4f}")
print(f"R-squared:     {r**2:.4f}")

# Scatterplot with regression line
x_line = np.linspace(0, 10, 100)
y_line = intercept + slope * x_line

plt.scatter(experience, salary, color="steelblue", label="Data")
plt.plot(x_line, y_line, color="firebrick",
         label=f"y = {intercept:.2f} + {slope:.2f}x")
plt.xlabel("Experience (years)")
plt.ylabel("Starting Salary ($1000s)")
plt.title("Least-Squares Regression: Experience vs. Starting Salary")
plt.legend()
plt.show()
