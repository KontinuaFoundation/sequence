import numpy as np
import matplotlib.pyplot as plt

# Replace with your data
data = np.array([250, 275, 310, 320, 350, 365, 410, 415, 430, 500, 525, 610, 720, 840])

# Choose bin edges (upper class boundaries are the right endpoints)
bins = np.arange(250, 851, 50)  # 250, 300, ..., 850

# Frequency in each bin
counts, edges = np.histogram(data, bins=bins)

# Cumulative frequency at each upper boundary
cumulative_counts = np.cumsum(counts)
upper_bounds = edges[1:]  # right endpoints

plt.plot(upper_bounds, cumulative_counts, marker='o')
plt.title("Cumulative Frequency Plot")
plt.xlabel("Upper class boundary ($)")
plt.ylabel("Cumulative frequency")
plt.grid(True)
plt.show()