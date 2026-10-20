# Positive Semidefinite Matrices — Notes

## Summary
Motivates NP problems and semidefinite programming, explains positive definite and semidefinite matrices through the scalar analogy and the elliptope, shows how AAᵀ builds a PSD matrix, and applies the Goemans-Williamson relaxation to Max Cut with a cvxpy script.

## Strengths
- Clear scalar intuition for "same side" versus "flipped" results.
- The elliptope example is correct: (0,0,0) gives a PSD matrix, and (2,2,2) does not.
- The Max Cut edge list matches the figure, and the relaxation steps are explained in order.

## Weaknesses
- **Wrong exercise answer:** the matrix [[2,2],[2,0]] has eigenvalues 1 ± √5 (about 3.24 and −1.24), so it is not positive definite. The answer "Yes, eigenvalues 2, 2" is wrong.
- **Python typo:** `05.*(1 - X[i,j])` is 5.0, not 0.5, so the objective is scaled by 10 and the printed value is wrong.
- **Imprecise claim:** "the chance of making the max cut is 0.5" should say the expected cut is half the edges. The 0.87 figure is the approximation ratio (about 0.878).
- **Unverified claim:** the figure's cut of 5 is not checked.
- **Definition:** "Positive semidefinite means x ≥ 0" omits the xᵀAx quadratic form.
- **Dependencies:** cvxpy is not listed in the setup instructions.

## Index entries added
NP problems, positive definite matrix, positive semidefinite matrix (three entries), elliptope, Goemans-Williamson technique, rounding, semidefinite programming, relaxation.

## Editor to-do
- Replace the exercise answer and fix the 05. coefficient.
- Reword the 0.5 probability claim and list cvxpy as a dependency.
