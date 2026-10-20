# Multiple Logistic Regression — Notes

## Summary
Extends logistic regression to several predictors, with the log-odds model and the logistic form of P(Y = 1 | x). The worked example uses hours studied and prior course completion (β₀ = −3, β₁ = 0.5, β₂ = 1): a student with 4 hours and the prior course has P = 0.5, and a student with 2 hours and no prior course has P ≈ 0.119. It also covers the coefficient interpretation, the divide-by-4 rule, and model checking. It has two exercises.

## Changes in this pass
- None to the text. The arithmetic was checked and is correct.

## Checked and correct
- η = −3 + 2 + 1 = 0, so P = 0.5. η = −2 at 2 hours and no prior course, so P = 1/(1 + e²) ≈ 0.119.
- Odds ratio for hours: e^{0.5} ≈ 1.649. For the prior course: e ≈ 2.718.
- Exercise mlog1: 6 hours and no prior course gives η = 0 and P = 0.5.
- The divide-by-4 rule: the logistic slope at P = 0.5 is 1/4, so a coefficient β_i changes P by about β_i/4 near the midpoint.

## Open items
- The chapter has one worked example. A second worked example, such as a numerical check of the divide-by-4 rule against the exact probability, would strengthen the section.
- The model-checking section is brief. It mentions the likelihood ratio test and correlated predictors but does not show how to compute either.
