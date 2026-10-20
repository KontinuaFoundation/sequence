# Bayesian Classifiers — Notes

## Summary
Builds a fish classifier for trout, bass, and catfish. It starts from the prior (121, 154, and 25 out of 300), uses naive Bayes with a normal density for each trait, and then uses a multivariate Gaussian with a covariance matrix. The worked example for a 16-inch, 2.1 kg fish gives P(bass | observation) ≈ 0.714 (naive) and 0.682 (multivariate). It ends with two exercises: a 13-inch, 1.9 kg fish (trout, ≈ 0.95) and an explanation of why the catfish posterior is nearly 0.

## Changes in this pass
- Fixed the catfish weight density. It was listed as 0.01. With μ = 3.42 and σ² = 0.0724, the density at 2.1 kg is about 8.3 × 10⁻⁶.
- Fixed the catfish joint probability in the naive table. It was 0.00001; it is now ≈ 0 (about 2 × 10⁻⁷).
- Fixed the final example. It said 19 inches, but the numbers are for 16 inches.
- Replaced "length and width" with "length and weight" (three places). The second trait is weight.
- Fixed the mean formula sum index (from d to n), and the variance formula (x_i − μ)².
- The covariance formula now divides by n − 1, which matches the diagonal values in the table. The text now says so, and notes that numpy's default does the same.
- "given the breed" → "given the species"; "::" → ":"; removed a stray comma in the trout covariance matrix.
- Added two exercises (13 inches, 1.9 kg → trout ≈ 0.948; catfish posterior nearly 0 despite an 8.3% prior).

## Checked and correct
- Priors: 0.403, 0.513, 0.083.
- Naive per-trait densities: trout 0.0546 and 0.7607; bass 0.1418 and 0.5753; catfish 0.2516 for length.
- Naive joint probabilities: trout 0.016763 and bass 0.041886. Posteriors: 0.286 (trout) and 0.714 (bass).
- Multivariate likelihoods: trout 0.04578, bass 0.07732, catfish ≈ 4.3 × 10⁻⁶. Joint probabilities: 0.01847 and 0.03969. Sum 0.0582. Posteriors: 0.318 (trout) and 0.682 (bass).

## Open items
- The multivariate catfish likelihood is shown as 0.000001. The computed value is about 4 × 10⁻⁶; a more exact figure would be better.
- The data and code (make_data.py, 1_scatter_fish.py, 2_univariates.py, 4_indep_density.png, 5_full.png) are referenced but not in this chapter directory. They were not checked.
- The chapter uses "height" language in the scatter-plot intro ("length and width (respectively)") that the figures may still reflect. Check the figure labels.
