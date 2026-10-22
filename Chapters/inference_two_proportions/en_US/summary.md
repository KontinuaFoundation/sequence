# Inference for Two Proportions: Summary

## What the chapter covers
Compares two population proportions:
- the parameter p₁ − p₂ and the sampling distribution of p̂₁ − p̂₂ ('variances add, even when you subtract'), with a simulation showing why;
- the Random, 10%, and large-counts conditions;
- the two-proportion z-interval (a sleep survey whose interval contains 0);
- the two-proportion z-test with a pooled proportion (a randomized text-reminder experiment, z = 2.14, p = 0.016), and why pooling is used for tests but not intervals;
- causation from randomized experiments vs. observational studies;
- Excel and statsmodels.

## Key ideas
- Standard deviation of p̂₁ − p̂₂: √(p₁(1−p₁)/n₁ + p₂(1−p₂)/n₂); variances add for differences.
- Interval: (p̂₁ − p̂₂) ± z*·SE, with unpooled SE; an interval containing 0 is not convincing evidence of a difference.
- Test of H₀: p₁ = p₂ uses the pooled p̂_c = total successes / total n.
- Only a randomized experiment supports a cause-and-effect conclusion.

## Changes in this pass
- New chapter, placed in volume 30 right after inferences_means (which has the two-sample t procedures this parallels) and two chapters after sampling_clt.
- Moved the 'two_sample_proportions' covers entry here from inferences_proportion's digital_resources.json. That chapter claimed the topic but never taught it.
- Includes a seeded simulation (difference_simulation.py, showing sd 0.0439 vs. 0.0006 if the sds were wrongly subtracted), a statsmodels listing (two_proportions.py) with real output, and 5 exercises with answers (biking interval, math-app test, reading an interval, pooling, Type I/II errors).
- Every value was checked against statsmodels (proportions_ztest and confint_proportions_2indep).
