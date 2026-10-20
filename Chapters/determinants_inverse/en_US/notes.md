# Determinants and Inverse Matrices — Notes

## Summary
Presents determinants as area and volume (2×2 and scaling by c²), links a zero determinant to dependent columns, gives the 3×3 rule (with a Sarrus-style diagram), a recursive cofactor-expansion Python function, the 2×2 and augmented-matrix inverse methods, A⁻¹ for solving Ax = b, and NumPy inverse and singular-matrix checks.

## Strengths
- The area exercise (13, 20, and −10 with area 10) and the 2×2 and 3×3 inverse answers are correct; the 3×3 inverse verifies by AA⁻¹ = I.
- The 2×2 inverse of [[1, 2], [0, −1]] is correct, and the Ax = b example (x = (2, 1)) checks out.
- The scaling argument det(cA) = c²det(A) is correct.

## Weaknesses
- **Wrong description:** a parallelepiped is three-dimensional, not "a six-dimensional figure formed by six parallelograms."
- **Undefined names:** the Python `if np.linalg.det(D) != 0` snippet uses D and e, which are not defined in this chapter.
- **Typo:** "apprend new row"; "Modify your code so that is uses"; "We find it's inverse".
- **Unclear sentence:** the 2×2 area exercise's last answer says "We will discuss this unusual response in a future chapter" without saying why the determinant is negative (orientation).

## Index entries added
parallelogram area, determinant!scaling, singular matrix, cofactor expansion, Sarrus rule, inverse!2 by 2 formula, inverse!augmented matrix method, linear system!inverse solution.

## Editor to-do
- Fix the parallelepiped description and define the Python variables.
- Explain the sign of the determinant (orientation) in the exercise answer.

