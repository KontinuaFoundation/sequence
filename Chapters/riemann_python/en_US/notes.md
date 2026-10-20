# Riemann Sums in Code and Practice — Notes

## Summary
Builds a riemann.py program that computes a left Riemann sum of 1/x and plots it, shows the expected output, and gives a table of L_n values that converge to ln 5. Then practices with a tank-filling table, a midpoint sum of x − 2 ln x, and a car velocity graph converted to meters.

## Changes in this pass
- Fixed the import: Rectangle comes from matplotlib.patches, not matplotlib.table.
- Fixed a missing parenthesis in the midpoint answer (sum = 3.84281).
- Fixed a stray "ß" and the unit "ms/s" (should be m/s).

## Strengths
- The sample terminal output matches the program's logic for a step size of 0.4.
- The L_n table matches the expected error about 1.6/n (for example, L_50 ≈ 1.6419 and L_5000 ≈ 1.6098).
- The tank answer (114.9 L) and the midpoint answers are correct.

## Open items
- The program has not been run in this pass. Run it to confirm the output lines.
- The car velocity answer uses converted speeds that are rough readings from the graph. The answer already says so.
