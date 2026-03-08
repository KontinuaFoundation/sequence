import matplotlib.pyplot as plt

# Replace this list with your data
data = [250, 275, 310, 320, 350, 365, 410, 415, 430, 500, 525, 610, 720, 840]

# Choose the number of bins (try changing this!)
plt.hist(data, bins=8)

plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()