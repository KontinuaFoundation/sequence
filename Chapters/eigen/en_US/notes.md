# Eigenvectors and Eigenvalues — Notes

## Summary
Defines eigenvectors and eigenvalues (Av = λv), the characteristic equation det(A − λI) = 0, and computes eigenvectors for [[5, 4], [1, 2]] (λ = 6, 1) and [[1, 2], [2, −2]] (λ = 2, −3). Also introduces eigenspaces and eigenbases, a NumPy eig example, and a summary of which transformations have invariant directions.

## Strengths
- Both worked 2×2 examples are correct: eigenvalues 6 and 1 with eigenvectors [4, 1] and [−1, 1]; eigenvalues 2 and −3 with eigenvectors [2, 1] and [1, −2].
- The reflection eigenvalues (1 and −1) and the shear's single invariant direction are stated correctly.
- The intuition sections (stays on the same line, scaled by λ) are clear.

## Weaknesses
- **Wrong rotation claim:** "rotations ... have no real eigenvectors (except the trivial cases θ = π/2 or 0)." A 90° rotation has no real eigenvectors. The exceptions are θ = 0 (identity) and θ = π (every vector has eigenvalue −1).
- **Overgeneralized scaling claim:** "scaling transformations preserve all directions" is true only for uniform scaling (kI). A diagonal scaling such as diag(2, 1) keeps only two directions.
- **Typos:** "doesn not change direction"; "add λ along the diagonal of a"; "cardinal scaling of its length".
- **Open FIXME:** "visual representation graphically?"
- **Historical claim:** the word "eigen" is attributed to David Hilbert; this is commonly cited, but should be checked against a reference before publication.

## Index entries added
eigenspace, characteristic equation, eigenequation, eigenvector!reflections, eigenvector!rotations, numpy!eig.

## Editor to-do
- Correct the rotation exception list and qualify the scaling claim.
- Fix the typos and resolve the FIXME; verify the Hilbert attribution.

