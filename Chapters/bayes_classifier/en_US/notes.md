# Bayesian Classifiers — Notes

## Summary
Builds a fish classifier for trout, bass, and catfish. Covers priors from counts, naive Bayes with per-trait normal densities, and a multivariate Gaussian with covariance. The worked example for a 16-inch, 2.1 kg fish gives P(bass | observation) ≈ 0.71 (naive) and 0.68 (multivariate).

## Strengths
- The priors are correct (121, 154, and 25 out of 300).
- The univariate densities and the multivariate densities (0.04578 for trout, 0.07732 for bass) match a recomputation.
- The posterior values (0.286/0.714 naive; 0.318/0.682 multivariate) match the joint probabilities.

## Weaknesses
- **Wrong probability:** p(W = 2.1 | catfish) is listed as 0.01. Using μ = 3.42 and σ² = 0.072, the density is about 8 × 10⁻⁶.
- **Wrong length in the final example:** the closing paragraph says "19 inches long," but the numbers computed are for 16 inches.
- **Mislabeled variable:** the text says "length and width" throughout, but the second trait is weight.
- **Inconsistent variance:** the univariate σ² uses 1/n, while the covariance diagonal uses n−1 (the ratio is exactly n/(n−1)). The text formulas show 1/n for both.
- **Wrong index:** the mean formula sums to d, but it should sum to n.
- **Wrong term:** "conditionally independent given the breed" should be species.
- **Typos:** "generalization of the normal distribution::" has a double colon.

## Index entries added
Bayesian classifier, prior probability, naive Bayes, conditional independence, multivariate Gaussian distribution, covariance matrix, maximum likelihood estimator.

## Editor to-do
- Fix the catfish density, the 19-inch sentence, and "width."
- Use one variance normalization everywhere and fix the sum index.
