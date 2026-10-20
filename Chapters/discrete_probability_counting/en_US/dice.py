import random
import matplotlib.pyplot as plt

# Can't ever be 0 or 1
p = [0.0, 0.0, 1/36, 1/18, 1/12, 1/9, 5/36, 1/6, 5/36, 1/9, 1/12, 1/18, 1/36]
roll_count = 1000

# Make an array containing 13 zeros
counts = [0] * 13

for i in range(roll_count):
    a = random.randrange(6) + 1
    b = random.randrange(6) + 1
    roll = a + b
    print(f"Round {i}: {a} + {b} = {roll}")

    # Increment the count for roll
    counts[roll] += 1

bar_width = 0.35
expected = []
actual_starts = []
expected_starts = []
labels = []
actual = []
for i in range(2,13):
    expected.append(p[i] * roll_count)
    actual.append(counts[i])
    actual_starts.append(i - bar_width/2)
    expected_starts.append(i + bar_width/2)
    labels.append(i)

fig, ax = plt.subplots()
ax.bar(actual_starts, actual, bar_width, label='Actual')
ax.bar(expected_starts, expected, bar_width, label='Expected')
ax.set_ylabel('Occurrences')
ax.set_title('Dice Rolls')
ax.set_xticks(labels)
ax.legend()
plt.show()
