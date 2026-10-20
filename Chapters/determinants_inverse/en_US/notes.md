# Determinants and Inverse Matrices — Notes

## Summary
Presents determinants as area and volume (2×2 and scaling by c²), links a zero determinant to dependent columns, gives the 3×3 rule (with a Sarrus-style diagram), a recursive cofactor-expansion Python function, the 2×2 and augmented-matrix inverse methods, A⁻¹ for solving Ax = b, and NumPy inverse and singular-matrix checks.

## Changes in this pass
- Corrected "six-dimensional" to "three-dimensional box" for a parallelepiped.
- Added a rectangle-area picture to the opening, and a worked 2×2 inverse example (A = [[3, 1], [5, 2]] gives A⁻¹ = [[2, −1], [−5, 3]]).
- Corrected the claim that NumPy's det uses the same recursion. NumPy uses LU decomposition.
- Replaced the Sarrus description. It is a set of products, not a recursion.
- Fixed the garbled sentence on the 2×2 inverse formula, and the garbled summary sentence on scaling.
- Explained the negative determinant in the rectangle exercise (orientation), and gave the area as 10.
- Replaced a NumPy snippet that showed a raise statement with code that really raises the error.
- Defined D and e in the Python snippet, and fixed "apprend," "so that is uses," "below the hood," and "We find it is inverse."
- Removed an empty duplicate subsection heading.
- Rewrote the sentence that said inverses are for non-square matrices as well.

## Strengths
- The area exercise (13, 20, and −10 with area 10) and the 2×2 and 3×3 inverse answers are correct. The 3×3 inverse verifies by AA⁻¹ = I.
- The 2×2 inverse of [[1, 2], [0, −1]] is correct, and the Ax = b example (x = (2, 1)) checks out.
- The scaling argument det(cA) = c²det(A) is correct.

## Open items
- The Python snippet that uses `np.linalg.solve` is not runnable as shown. It is a fragment that needs D and e defined first. A full version would help.
