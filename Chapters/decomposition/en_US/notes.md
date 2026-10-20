# Singular Value Decomposition — Notes

## Summary
Defines A = UΣVᵀ (U from AAᵀ, V from AᵀA, Σ from singular values), works a 2×3 example by hand (eigenvalues 12 and 10), shows a NumPy SVD and reconstruction, discusses sign ambiguity, and uses SVD on a black-and-white pixel image.

## Strengths
- The AAᵀ, AᵀA, eigenvalue, and eigenvector computations are correct, and Vᵀ is correct.
- UΣVᵀ = A checks out when Σ uses √12 and √10.
- The NumPy singular values [3.4641, 3.1623] and the exercise answer's signs match the hand computation (sign ambiguity).
- The image's singular values 6.79 and 3.72 are correct (checked with NumPy), and the 62-value count is correct.

## Weaknesses
- **Wrong Σ:** the Σ matrix writes √12 twice. The second singular value is √10, as the product step shows.
- **Repeated label:** "For λ = 10" is used for the second eigenvalue, which should be λ = 12.
- **Dimension mismatch:** the displayed pixel matrix has 10 rows of 20 entries, but the text calls it 20 × 10.
- **Typo:** the A^TA product has a stray "&" in the second matrix.
- **Imports:** the Python code uses scipy, which is not in the chapter's list of dependencies.

## Index entries added
singular values, singular vectors, sign ambiguity, image compression, low-rank approximation, principal component analysis, SVD manual calculation, orthogonal matrix.

## Editor to-do
- Correct Σ and the λ label; reconcile the image dimensions.
- Add scipy to the setup instructions.
