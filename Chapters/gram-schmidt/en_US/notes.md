# The Gram-Schmidt Process — Notes

## Summary
Presents Gram-Schmidt for orthogonalizing a linearly independent set using projections, with historical notes (Gram 1883, Schmidt 1907), the procedure, normalization, a three-vector worked example, a two-vector exercise, and a NumPy script.

## Strengths
- The worked example's orthogonal vectors (1, 2, −2), (0, −2, −2), (4, −1, 1) and their normalized forms are correct.
- The exercise's v₂ = (−2/3, 1/3, 1/3) and its normalized form (−0.816, 0.408, 0.408) are correct.
- The Python script implements the projection subtraction correctly.

## Weaknesses
- **Wrong v₃ derivation:** the second projection uses x₂ = (1, 0, −4) instead of v₂ = (0, −2, −2), so the coefficient −4/8 is also wrong (x₃·x₂ = 5, x₂·x₂ = 17). The line (1/2)(1, 0, −4) → (0, −1, −1) is wrong too. The final v₃ = (4, −1, 1) is still correct.
- **Exercise typos:** the denominator "(1,1,1)(1,1,−1)" should be (1,1,1)·(1,1,1) = 3. The normalization lines write v/√|v| and "(0, 1, 1)√|v₂|", which are not the norm formula.
- **Code comment:** "projection of x3 on v3" should read v2.

## Index entries added
Gram-Schmidt procedure, orthonormal set, Gram-Schmidt example, Gram-Schmidt history, orthogonal basis, Gram-Schmidt applications.

## Editor to-do
- Correct the v₃ derivation and the exercise's normalization formulas.
- Fix the code comment.
