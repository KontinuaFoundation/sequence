import random
from collections import Counter

random.seed(5)

def triple_birthday(people, trials=10_000):
    hits = 0
    for _ in range(trials):
        counts = Counter(random.randrange(365) for _ in range(people))
        if max(counts.values()) >= 3:      # some day has 3 or more people
            hits += 1
    return hits / trials

for n in [23, 50, 80, 88, 100]:
    print(n, triple_birthday(n))
