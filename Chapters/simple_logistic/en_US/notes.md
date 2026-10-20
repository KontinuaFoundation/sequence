# Simple Logistic Regression — Notes

## Summary
Introduces logistic regression for a binary response: the log-odds model ln(p/(1−p)) = β₀ + β₁x, the resulting S-shaped p(x), maximum likelihood estimation, the odds interpretation of β₁ (each unit multiplies the odds by e^{β₁}), and a threshold rule. It uses β₀ = −4, β₁ = 1 as the running example and has three exercises (p(2) ≈ 0.119, the x where p = 0.5 is 4, and an odds factor of e^{0.5} ≈ 1.649).

## Changes in this pass
- Added a high school link: x is hours of study and Y = 1 means the student passes a test.

## Checked and correct
- p(3) ≈ 0.269, p(4) = 0.5, p(5) ≈ 0.731 for β₀ = −4, β₁ = 1.
- Odds at x = 3 are e⁻¹ ≈ 0.368, and at x = 4 they are 1.
- p(2) ≈ 0.119.
- e^{0.5} ≈ 1.649, an increase of about 65% in the odds.
- Threshold 0.5 gives the cutoff x ≥ 4 for this model.

## Open items
- The chapter has no fully worked example with data. The running example works through formulas. A short worked example with a small table of outcomes would match the standard format.
- The maximum likelihood section is brief. A sentence on the likelihood function would help readers who have seen it before.
