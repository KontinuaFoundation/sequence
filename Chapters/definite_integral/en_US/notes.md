# Definite Integrals — Notes

## Summary
Defines the definite integral as the limit of Riemann sums, explains signed area, proves the a = b case, and covers the constant-multiple, sum/difference, adjacent-interval, bounding, and reversed-limit properties. Applies integrals to displacement (10 − 8 = 2 m), work and kinetic energy (1 J, 0.816 m/s), and impulse, then gives practice problems.

## Strengths
- The displacement example is correct: the positive area is 10 m and the negative area is 8 m, so displacement is 2 m.
- The box example is correct: W = ∫₀² 0.5x dx = 1 J, and v = √(2/3) ≈ 0.816 m/s.
- The practice answers are correct: ∫₀¹(5 − 6x²) dx = 3, the AP 2012 table-based answers (0, 27.5, and B), and ∫₋₁⁹ g = 2.5.
- The reversed-limits proof is clean.

## Weaknesses
- **Index typo:** \index{definite integra;} should read "definite integral."
- **Wrong variable:** v(t) = sin(πx) mixes t and x.
- **Answer notation:** the exercise answer writes f(x) where f(x_i) is meant inside the sum.
- **Weak argument:** the a = b argument takes lim (b − a)·lim f/n, which is a 0·∞ form, so it does not prove the result rigorously. The width argument (Δx = 0) is enough.
- **Typos:** "over the for a ≤ x ≤ b," "axisj," a stray "=" in the B-case explanation, and "$x-axis$" in math mode.

## Index entries added
definite integral (corrected entry), net area, displacement (from velocity), work (integral), impulse, reversed limits, bounds estimate.

## Editor to-do
- Fix the index typo and the t/x variable.
- Replace the a = b argument with a width-based proof, and fix the typos.
