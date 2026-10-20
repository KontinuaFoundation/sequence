# Double Integrals over Rectangular Regions — Notes

## Summary
Introduces volume under a surface over a rectangle by subdividing into columns and defining the double integral, then covers iterated integrals (the 21/2 example), order exchange, Fubini's theorem, and evaluations including 5/2 − 1/e, 18, 6, 9 ln 5, (π/6) ln 2, and a sin(x+y) integral with exact result (6√3 − 6 − π)/12.

## Changes in this pass
- Fixed the definition of the subrectangle R_ij. It is now the set {(x, y) | x_{i−1} ≤ x ≤ x_i, y_{j−1} ≤ y ≤ y_j}, not a rectangle minus a set.
- Fixed "f(x,y) in continuous" to "is continuous" and "θ = o" to "θ = 0."
- Replaced the garbled sentence about partial differentiation. Integrating with respect to x, with y held constant, reverses a partial derivative in x.
- Added a garden-and-hill picture before the graph of f over R, as a high school link.

## Checked and correct
- Iterated integral ∫₀³∫₁² xy² dy dx = 21/2, and the reversed order also gives 21/2.
- The practice answers: 5/2 − 1/e, 18, 6.
- Fubini answers (the 9 ln 5 and (π/6) ln 2 integrals). The sin(x+y) answer (6√3 − 6 − π)/12 ≈ 0.1042, rechecked by hand through the expansion sin(x+y) and integration by parts.

## Open items
- The exercise label `iterate_1` matches its answer. The earlier note about a space in the label was stale.
- The partial-derivative description is now one line. The notation $\int$ vs. $\iint$ is consistent in the Fubini box but not in the Riemann-sum section.
