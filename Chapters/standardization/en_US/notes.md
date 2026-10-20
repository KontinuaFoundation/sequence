# Standardizing Data — Notes

## Summary
Defines standardization Z = (X − μ)/σ, works the values 2, 4, 6, 8 (μ = 5, σ ≈ 2.236, Z = −1.342, −0.447, 0.447, 1.342), and explains why standardization matters for gradient descent, k-NN, regularized regression, principal components, and coefficient comparison. It includes two cautions (standardization does not change shape; tree models do not need it; compute μ and σ from the training set only) and two exercises.

## Changes in this pass
- Reworded the first caution. Standardization does not change the shape of a distribution. It sets the mean to 0 and the standard deviation to 1. The old wording about "equal variance in any deep sense" was unclear.
- Added a high school link: comparing a math test and a science test with the z-score.

## Checked and correct
- Worked example: σ = √5 ≈ 2.236, and the four Z-values are −1.342, −0.447, 0.447, 1.342.
- Exercise std1: Z = (65 − 50)/10 = 1.5.
- The leakage answer matches the rule that μ and σ come from the training set only.

## Open items
- The worked example uses the population standard deviation (divide by n). The sample standard deviation (divide by n − 1) would give different values. The text states which one is used, so this is consistent, but a note on the other convention would help.
