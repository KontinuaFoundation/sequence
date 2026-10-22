import random
import math

random.seed(1)                      # same "random" darts every run

def estimate_pi(darts):
    inside = 0
    for _ in range(darts):
        x = random.random()         # a random number from 0 to 1
        y = random.random()
        if x**2 + y**2 <= 1:        # inside the quarter circle?
            inside += 1
    return 4 * inside / darts

for darts in [100, 10_000, 1_000_000]:
    estimate = estimate_pi(darts)
    print(f"{darts:>9} darts: {estimate:.5f}  (error {abs(estimate - math.pi):.5f})")
