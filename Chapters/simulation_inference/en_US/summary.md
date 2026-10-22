# Simulation-Based Inference: Summary

## What the chapter covers
Introduces inference by computer simulation, before the formula-based chapters:
- the bootstrap (resampling the sample with replacement) for a standard error and a 95% percentile interval for mean sleep hours, matching σ/√n from the CLT chapter, then bootstrapping a median;
- the limits of the bootstrap (it cannot fix a biased sample);
- the permutation test (shuffling group labels in a randomized music-vs-silence experiment) for a p-value of about 0.008, close to the later t-test's 0.007;
- why shuffling works, and a common p-value misinterpretation.

## Key ideas
- Bootstrap: resample the sample with replacement; the spread of the resampled statistic estimates its standard error.
- A 95% percentile interval is the middle 95% of the bootstrap statistics; it works for medians and other statistics without formulas.
- Permutation test: if the treatment does nothing, the labels are arbitrary; shuffling them builds the null distribution.
- The p-value is computed assuming the null hypothesis; it is not the probability that the null is true.

## Changes in this pass
- New chapter, placed in volume 30 right after sampling_clt and before inferences_proportion, so students meet intervals and p-values through simulation before the formulas.
- Results checked against the formula methods taught later (bootstrap SE 0.250 vs. s/√n 0.253; permutation p 0.0083 vs. Welch t 0.0072; the proportion exercise's 0.047 vs. Fisher's exact 0.048).
- Added a pointer from bagging_random_forest's bootstrap sample back to this chapter.
- Includes two seeded listings (bootstrap.py, permutation.py) with real output, two figures (bootstrap.png, permutation.png), and 5 exercises with answers (bootstrap samples by hand, bootstrapping a median, a permutation test for a warm-up routine, what a p-value means, bootstrap or permutation?).
