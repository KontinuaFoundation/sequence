import random

random.seed(4)

def shared_birthday(people, trials=20_000):
    hits = 0
    for _ in range(trials):
        birthdays = [random.randrange(365) for _ in range(people)]
        if len(set(birthdays)) < people:   # a set drops repeats
            hits += 1
    return hits / trials

def exact(people):
    no_match = 1
    for i in range(people):
        no_match *= (365 - i) / 365
    return 1 - no_match

for n in [10, 23, 30, 50]:
    print(f"{n} people: simulated {shared_birthday(n):.3f}, exact {exact(n):.3f}")
