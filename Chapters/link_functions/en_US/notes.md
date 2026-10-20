# Link Functions — Notes

## Summary
Defines the link g(μ) = η and its inverse, lists identity, log, logit, and probit links with their ranges, works the logit of 0.8 (ln 4 ≈ 1.386) and the log of 10 (ln 10 ≈ 2.303) with their inverses, and explains how to choose a link and how coefficients change meaning. It has two exercises (the logit of 0.25 is about −1.099, and a log-link coefficient of 0.2 multiplies the mean by about 1.221).

## Changes in this pass
- Added a high school link: a test score can be any number (identity link), but a chance of passing must stay between 0 and 1 (logit link).

## Checked and correct
- logit(0.8) = ln 4 ≈ 1.386, and the inverse logit returns 0.8.
- ln 10 ≈ 2.303, and e^{2.303} = 10.
- Exercise lf1: logit(0.25) = ln(1/3) ≈ −1.099.
- Exercise lf2: e^{0.2} ≈ 1.221.

## Open items
- The probit section defines the link but gives no numerical example. A value such as Φ⁻¹(0.975) ≈ 1.96 would make it concrete.
- The chapter does not show the complementary log-log link, which some GLM software offers. A sentence noting that other links exist would help.
