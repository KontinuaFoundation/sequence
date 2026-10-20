# Positive Semidefinite Matrices — Notes

## Summary
Motivates NP problems and semidefinite programming, explains positive definite and semidefinite matrices through the scalar analogy and the elliptope, shows how AAᵀ builds a PSD matrix, and applies the Goemans-Williamson relaxation to Max Cut with a cvxpy script.

## Changes in this pass
- Fixed the first exercise. [[2, 2], [2, 0]] has eigenvalues 1 ± √5, so it is not positive definite. The answer now says "No" and shows why.
- Added a worked example: [[2, 1], [1, 2]] has eigenvalues 1 and 3, so it is positive definite.
- Added a worked answer for the open exercise: AAᵀ for a 3 × 3 matrix, with eigenvalues 9 and 3 ± 2√2.
- Wrote the definitions with the quadratic form xᵀAx (positive definite > 0, positive semidefinite ≥ 0 for every x).
- Fixed the Python coefficient `05.` to `0.5`, and the output comment.
- Replaced the claim that a random cut gets the max with 0.5 with the expected cut (half the edges). The approximation ratio is about 0.878.
- Verified that the figure's cut of 5 is the maximum: the triangle 1-3-4 can contribute at most two cut edges.
- Corrected the Clay Institute remark. Its prize is for the P versus NP question, not for Max Cut.
- Softened overclaims ("no algorithm", "guarantees an optimal solution"), and fixed the "previous workbook" reference.
- Listed the cvxpy and scipy installs.

## Strengths
- Clear scalar intuition for "same side" versus "flipped" results.
- The elliptope example is correct: (0, 0, 0) gives a PSD matrix, and (2, 2, 2) does not.
- The Max Cut edge list matches the figure, and the relaxation steps are in order.

## Open items
- The rounding step was described but not run. The cut of 5 is a best-possible value, not a guarantee of what the rounding finds.
