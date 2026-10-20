# The Gram-Schmidt Process — Notes

## Summary
Presents Gram-Schmidt for orthogonalizing a linearly independent set using projections, with historical notes (Gram 1883, Schmidt 1907), the procedure, normalization, a three-vector worked example, two exercises, and a NumPy script.

## Changes in this pass
- Corrected the v₃ derivation. The second projection now uses v₂ = (0, −2, −2), not x₂. The coefficient −4/8 is now correct, and the result (4, −1, 1) is unchanged.
- Fixed the exercise's denominator to (1,1,1)·(1,1,1) = 3, and replaced the garbled normalization lines with the correct lengths (√3 and √6/3).
- Fixed the code comment to say "projection of x3 on v2".
- Replaced the signal-processing application (not accurate as stated) with least-squares fitting.
- Added an unworked exercise: x₁ = (1, 0, 1), x₂ = (1, 1, 0) gives v₂ = (1, 2, −1) up to scale.

## Strengths
- The worked example's orthogonal vectors (1, 2, −2), (0, −2, −2), (4, −1, 1) and their normalized forms are correct.
- The original exercise's v₂ = (−2/3, 1/3, 1/3) and normalized form (−0.816, 0.408, 0.408) are correct.

## Open items
- None from this pass.
