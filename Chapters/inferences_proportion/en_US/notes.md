# Statistical Inferences for Proportions — Notes

## Summary
Introduces point estimates and confidence intervals, then builds the confidence interval for a proportion with a bike-lane survey (120 of 200 gives 0.60 ± 0.068, or (0.532, 0.668)), sample-size planning (n = 1068 for E = 0.03), and Excel and Python walkthroughs. Ends with an introduction to tests of significance.

## Changes in this pass
- Replaced the placeholder comments with content: the three conditions (random, 10%, large counts), the interval formula, the sample-size formula, and an example.
- Wrote the Excel walkthrough (NORM.S.INV, the margin of error, and the interval cells).
- Wrote the Python walkthrough with scipy (norm.ppf) and statsmodels (proportion_confint), plus a sample-size function.

## Strengths
- All worked numbers are correct: the standard error 0.0346, the margin of error 0.068, the interval (0.532, 0.668), and n = 1068.
- The intuition about confidence versus precision is clear.

## Open items
- The chapter ends at the start of tests of significance. The rest of the chapter is not written.
- The Python output for proportion_confint (method "normal") was checked by hand, not by running the code.
