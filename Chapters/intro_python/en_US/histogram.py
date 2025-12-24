import matplotlib.pyplot as plt

data = [4, 5, 5, 6, 7, 7, 7, 8, 8, 9, 10, 10, 10, 11, 12]

plt.hist(data, bins=5)
plt.title("Histogram of Values")
plt.xlabel("value")
plt.ylabel("frequency")
plt.show()