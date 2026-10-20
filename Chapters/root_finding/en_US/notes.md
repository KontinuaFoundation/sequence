# Numerical Root Finding — Notes

## Summary
Motivates numerical roots, then covers the bisection method (with the sign-change argument and a 19-step example to 10⁻⁶ for √2), Newton's method (iterates 1.5, 1.41667, 1.414216), Python code for both, a comparison of their speed and reliability, and three exercises.

## Changes in this pass
- None to the mathematics. All values were checked: the midpoint f(1.5) = 0.25, the 19 bisection steps for width 10⁻⁶ (the loop stops when (b − a)/2 ≤ tol), and the Newton iterates.

## Strengths
- The code and the explanations match, and the exercises have short answers.
- The comparison (bisection always converges with a sign change but gains one binary digit per step; Newton converges faster but can diverge) is accurate.

## Open items
- The printed outputs in the code block (1.4142141342163086 and 1.4142135623730951) were not regenerated in this pass.
