# Numerical Double Integration — Notes

## Summary
Revisits the snail distribution and asks for the probability that a snail's mass is in [3, 4] g and diameter in [1.5, 2.0] cm. Presents the double integral, the Riemann-sum idea extended to two dimensions, and a Python midpoint sum that gives 7.8316%.

## Strengths
- The Python result (7.8316%) reproduces when rerun.
- The motivation (no closed-form antiderivative) and the 2D Riemann-sum figures are clear.

## Weaknesses
- **Mean mismatch:** the text gives the snail mean as (4.25 g, 2.35 cm), but the code uses (4.3556, 2.3527). The 4.25 figure appears in the earlier chapter, so the two should agree.
- **Overstatement:** "no one has ever been able to find the antiderivative" overstates. The multivariate normal has no elementary antiderivative, but the claim should be limited to that case.
- **Method mismatch:** the text describes right-endpoint Riemann sums, but the code uses midpoints.
- **Odd setting:** "a snail off the floor of the ocean" does not match the earlier snail data, which has no location.
## Index entries added
multivariate normal distribution, Riemann sum, Riemann sum (two dimensions), numerical integration, numerical integration (python), double integral.

## Editor to-do
- Reconcile the mean vector and the covariance precision with the earlier chapter.
- Say which sum (left, right, or midpoint) the code uses.
