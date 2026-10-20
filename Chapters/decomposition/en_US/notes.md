# Singular Value Decomposition — Notes

## Summary
Defines A = UΣVᵀ (U from AAᵀ, V from AᵀA, Σ from singular values), works a 2×3 example by hand (eigenvalues 12 and 10), shows a NumPy/SciPy SVD and reconstruction, discusses sign ambiguity, and uses SVD on a black-and-white pixel image. Adds an unworked exercise on the singular values of a 2×2 matrix.

## Changes in this pass
- Corrected Σ. The second singular value is √10, not √12, in both the Σ matrix and the product step.
- Changed the λ = 10 label to λ = 12 for the second eigenvalue.
- Corrected the statement about shared eigenvalues. The nonzero eigenvalues of AAᵀ and AᵀA are the same. The text said "U" and "V".
- Removed a stray "U =" from the product step.
- Replaced "apply Gram-Schmidt" with normalization for the eigenvectors of AAᵀ, since they are already orthogonal.
- Fixed the image dimensions: the pixel matrix is 10 × 20, so u vectors have 10 entries and v vectors have 20. The count (62) is unchanged. Changed "columns" to "rows" in the image description, and added a striped-shirt picture.
- Noted that the Python example uses SciPy, and said how to install it.
- Added an unworked exercise: the singular values of [[0, 3], [0, 4]] are 5 and 0.

## Strengths
- The AAᵀ, AᵀA, eigenvalue, and eigenvector computations are correct, and Vᵀ is correct.
- UΣVᵀ = A checks out with Σ = [[√12, 0, 0], [0, √10, 0]].
- The exercise answer's signs match the hand computation (sign ambiguity).
- The image's singular values 6.79 and 3.72 and the 62-value count are correct.

## Open items
- The image singular values were checked against NumPy in an earlier pass. The chapter does not show the calculation. A short explanation would help.
