# Continuous Distributions — Notes

## Summary
Builds the CDF and PDF from cow weights, introduces the uniform distribution and SciPy functions, plots a normal distribution, then covers the normal distribution (with grade and parts examples), multivariate normal distributions for snails (mean vector, covariance matrix, density), PDFs and joint densities (with independent wait-time and snow examples), and exponential decay (carbon-14).

## Changes in this pass
- Fixed the normal pdf exponent: it is −(x − μ)²/(2σ²), not −(x − μ)/(2σ²).
- Corrected the carbon-14 answer: 1 − 1/e ≈ 63.2%, not 63.5%.
- Fixed the snow exercise. The humidity density integrated to 1/3, not 1. The corrected density is 6(100h − h²)/10⁶, and the answer is P = 5/64 ≈ 7.8% (the old answer gave 0.26%).
- Fixed "mean off" to "mean of."
- The covariance code now uses bias=True, so it divides by n (as the formula in the text does). np.cov otherwise divides by n − 1.

## Strengths
- The uniform, grade, SciPy, and decile values are correct (for example, the top-decile cutoff of 173.80 cm and 26.29% between 160 and 165 cm).
- The grade example (23.56%) and the parts example (82.24%) are correct.
- The joint density examples (C = 1/6750 and P(X ≥ Y) = 7/12) and the independent wait-time example (about 34.3%) are correct.

## Open items
- The multivariate section describes the snail data without printing the full data set. The example values are illustrative.
