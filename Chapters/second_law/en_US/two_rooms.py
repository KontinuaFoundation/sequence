import random
import matplotlib.pyplot as plt

plt.rcParams["font.size"] = 14
random.seed(1)
n = 100                      # number of molecules
left = [True] * n            # every molecule starts on the left
counts = [n]

for step in range(1000):
    i = random.randrange(n)  # pick a random molecule...
    left[i] = not left[i]    # ...and move it to the other side
    counts.append(sum(left))

print("after 1000 steps:", counts[-1], "on the left")
print("average of the last 500 steps:", sum(counts[500:]) / len(counts[500:]))
print("all on the left again?", n in counts[1:])

plt.plot(counts)
plt.axhline(n / 2, color="gray", linestyle="--")
plt.xlabel("step")
plt.ylabel("molecules on the left")
plt.ylim(0, n)
plt.tight_layout()
plt.savefig("two_rooms.png", dpi=150)
