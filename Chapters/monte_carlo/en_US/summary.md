# Monte Carlo Simulation: Summary

## What the chapter covers
Introduces Monte Carlo simulation: estimating probabilities and areas by running random experiments and counting. Covers Python's random library and seeds, why counting works (the Law of Large Numbers), estimating π with random darts and how the error shrinks like 1/√n, the full Monty Hall game (stay vs. switch, 10 doors, and 'Monty Fall', where a host who opens a random door gives no advantage), the birthday problem checked against the exact formula, and a question without an easy formula: when do three people likely share a birthday (88).

## Key ideas
- If you cannot calculate a probability, simulate it many times and count.
- random.random(), randrange, randint, choice; random.seed makes runs repeatable.
- Typical error shrinks like 1/√n: one more digit needs 100 times as many trials.
- In Monty Hall, the advantage of switching comes from the host's knowledge.

## Changes in this pass
- New chapter, placed in volume 10 right after paradoxes, as a bridge to the probability chapters in volume 28. It needs no counting formulas, only Python from volumes 3–4.
- Builds on paradoxes instead of repeating it: the full Monty Hall game replaces the shortcut used there, and the birthday simulation is checked against that chapter's exact formula. Added a one-line pointer from paradoxes to this chapter.
- Includes 5 Python programs with real, seeded output (estimate_pi.py, monty_hall.py, monty_fall.py, birthday.py, triple.py), two figures (darts.png, birthday.png), and 5 exercises with answers (darts by hand, four doors = 3/8, lucky seven, two heads in a row = 6, area under x² by darts).
- Every exercise answer was checked by simulation; forward references to the Limits chapter (volume 17) and the series chapters (volume 33) are stated as 'later'.
