import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
scores = [55, 60, 66, 72, 78, 85]

plt.scatter(hours, scores)
plt.title("Study Time vs. Score")
plt.xlabel("hours studied")
plt.ylabel("score")
plt.show()