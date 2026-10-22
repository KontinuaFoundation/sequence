import random

random.seed(10)

trials = 100_000
exactly_7 = 0
for _ in range(trials):
    made = sum(random.random() < 0.7 for _ in range(10))   # 10 shots
    if made == 7:
        exactly_7 += 1
print(exactly_7 / trials)
