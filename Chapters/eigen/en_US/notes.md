# Eigenvectors and Eigenvalues — Notes

## Summary
Defines eigenvectors and eigenvalues (Av = λv), the characteristic equation det(A − λI) = 0, and computes eigenvectors for [[5, 4], [1, 2]] (λ = 6, 1) and [[1, 2], [2, −2]] (λ = 2, −3). Adds an upper-triangular exercise, eigenspaces and eigenbases, a NumPy eig example, and a summary of which transformations have invariant directions.

## Changes in this pass
- Corrected the rotation claim. A 90° rotation has no real eigenvectors. θ = 0 (all vectors, eigenvalue 1) and θ = π (all vectors, eigenvalue −1) are the exceptions.
- Qualified the scaling claim. Only uniform scaling kI keeps every direction.
- Fixed "λ2" (rendered as λ followed by 2) to λ², and the "subtract λ from each diagonal entry" wording.
- Removed the visible FIXME and the duplicate \item, and replaced "O" with the zero vector.
- Fixed typos ("doesn not", "Once your find", "lets").
- Added a rubber-sheet picture for eigenvectors, and an unworked exercise on an upper-triangular matrix (eigenvalues 4 and 2; eigenvectors (1, 0) and (1, −2)).

## Strengths
- Both worked 2×2 examples are correct: eigenvalues 6 and 1 with eigenvectors (4, 1) and (−1, 1); eigenvalues 2 and −3 with eigenvectors (2, 1) and (1, −2).
- The reflection eigenvalues (1 and −1) and the shear's single invariant direction are correct.

## Open items
- The attribution of the word "eigen" to David Hilbert is commonly cited. Check it against a reference before publication.
