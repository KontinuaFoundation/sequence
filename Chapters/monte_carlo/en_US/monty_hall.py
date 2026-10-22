import random

random.seed(2)

def play(switch, doors=3):
    car = random.randrange(doors)
    pick = random.randrange(doors)
    # The host opens every other door except one, never revealing the car.
    if pick == car:
        # any other door can stay closed
        closed = random.choice([d for d in range(doors) if d != pick])
    else:
        closed = car
    if switch:
        pick = closed
    return pick == car

games = 100_000
for switch in [False, True]:
    wins = sum(play(switch) for _ in range(games))
    print("switch" if switch else "stay  ", wins / games)
print("10 doors, switch:", sum(play(True, 10) for _ in range(games)) / games)
