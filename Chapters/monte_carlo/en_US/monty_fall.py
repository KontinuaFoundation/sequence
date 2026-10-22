import random

random.seed(3)

kept = 0          # games where the host happened to show a goat
switch_wins = 0
for _ in range(100_000):
    car = random.randrange(3)
    pick = random.randrange(3)
    # The host slips and opens one of the other two doors at random.
    opened = random.choice([d for d in range(3) if d != pick])
    if opened == car:
        continue                       # car revealed: this game does not count
    kept += 1
    other = 3 - pick - opened          # the one remaining closed door
    if other == car:
        switch_wins += 1
print(kept, switch_wins / kept)
