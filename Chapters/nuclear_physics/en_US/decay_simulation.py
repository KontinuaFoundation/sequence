import random

random.seed(8)

atoms = 1000
STEPS_PER_HALF_LIFE = 10
# chance that one atom decays during one step (a tenth of a half-life)
p = 1 - 0.5 ** (1 / STEPS_PER_HALF_LIFE)

for half_life in range(1, 6):
    for _ in range(STEPS_PER_HALF_LIFE):
        # each surviving atom independently decays with probability p
        atoms = sum(1 for _ in range(atoms) if random.random() > p)
    print(f"after {half_life} half-lives: {atoms:4} atoms left "
          f"(formula: {1000 * 0.5 ** half_life:.1f})")
