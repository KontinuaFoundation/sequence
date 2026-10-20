# Slope Fields — Notes

## Summary
Introduces slope fields for y' = f(x, y): drawing ticks, filling in y' = 0 on y = −x for y' = x + y, sketching a solution through (1, 0), and an RL circuit example (dI/dt = 15 − 3I, equilibrium I = 5, solution I = 5 − 5e^{−3t}). Ends with a practice exercise for y' = x + y².

## Changes in this pass
- Fixed the spelling of Kirchhoff's law.
- Reworded "the slope will be the same of all values of t" to "the slope is the same for all values of t at a given I."

## Strengths
- The solution sketch for y' = x + y through (1, 0) is correct: y = −x − 1 + 2e^{x−1}.
- The circuit equation is correct (V = L dI/dt + RI, giving dI/dt = 15 − 3I), with the equilibrium at 5 A.
- The field and sketch are consistent with the equilibrium.

## Open items
- The slope-field figures are hand-coded tick lists. Consider generating them with Python so they are accurate.
