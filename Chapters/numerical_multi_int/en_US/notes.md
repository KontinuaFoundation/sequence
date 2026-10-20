# Numerical Double Integration — Notes

## Summary
Revisits the snail distribution and asks for the probability that a snail's mass is in [3, 4] g and diameter in [1.5, 2.0] cm. Presents the double integral, explains why it has no closed form, extends the Riemann-sum idea to two dimensions with figures, and gives a Python midpoint sum that gives 7.8316%.

## Changes in this pass
- Made the mean match the code. The text now gives μ = (4.36 g, 2.35 cm), which rounds the value used in the code (4.3556, 2.3527).
- Replaced "no one has ever been able to find the antiderivative" with the accurate statement that the multivariable normal density has no elementary antiderivative.
- Stated that the code uses a midpoint Riemann sum (the 1D figure still shows right endpoints, which is a separate picture).
- Renamed the variable `sum` to `total` in the Python code, so it no longer shadows the built-in `sum`.
- Fixed the inequality signs in the rectangle description (`<=` to `\leq`).

## Checked and correct
- The probability 7.8316% is what the midpoint sum returns with 100 × 100 slices.
- The covariance matrix in the text matches the one in the code.

## Open items
- The earlier multivariate normal chapter should use the same mean. It was not reopened in this pass; check whether it shows 4.25 or 4.36.
- The opening sentence says "a snail off the floor of the ocean." This is a whimsical setting, not something the data supports. It can stay or be removed.
- The Riemann-sum figure uses right endpoints. The code uses midpoints. A brief caption note would make the difference clear.
