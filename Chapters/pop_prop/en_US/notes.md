# Population Proportion Statistics — Notes

## Summary
Builds from the binomial distribution for a 12-voter sample (r = 0.62) to the likelihood of an observed 9-of-12 result, then to a posterior density under a uniform prior, identifies it as a Beta(k+1, n−k+1) distribution, and gives a scipy calculation that P(r > 0.5) ≈ 95.39%.

## Strengths
- The binomial probability table is correct (checked each entry; the k = 8 mode of 0.2254 is right).
- The 9-of-12 likelihoods are correct: 1.6 × 10⁻⁷ at r = 0.1 and 0.2397 at r = 0.7.
- The beta result is correct: scipy's P(r > 0.5) matches a numerical integration (95.39%).
- The step from likelihood to density (uniform prior, normalizing) is clear.

## Weaknesses
- **Typo:** "This is a called a likelihood" should read "This is called a likelihood."
- **Likelihood wording:** the claim that the likelihood's area is "significantly less" than 1 should give the actual area (about 1/13) or say why.
- **Unused import:** numpy is imported but not used in the Python block.
- **Missing exercise:** no practice problem.

## Index entries added
binomial distribution, likelihood, maximum likelihood estimator, Bayes' theorem (continuous), beta distribution.

## Editor to-do
- Fix the "a called" typo and remove the numpy import.
- Add an exercise.
