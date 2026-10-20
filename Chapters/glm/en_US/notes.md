# Generalized Linear Models — Notes

## Summary
Introduces generalized linear models with three components (random, systematic, and link), explains how the distribution and link are chosen, and works a Poisson example with the log link (η = 0.5 + 0.2 × 3 = 1.1, so E[Y] = e^{1.1} ≈ 3.004 customers). It notes that GLM parameters are fit by maximum likelihood and that logistic and ordinary linear regression are special cases. It has two exercises (E[Y] = e^{1.5} ≈ 4.48 at x = 5, and naming the model for a yes-or-no vote).

## Changes in this pass
- None to the text. The arithmetic was checked and is correct.

## Checked and correct
- η = 1.1 at x = 3, E[Y] = e^{1.1} ≈ 3.004.
- Exercise glm1: η = 1.5 at x = 5, E[Y] = e^{1.5} ≈ 4.48.
- Exercise glm2: a binomial response with the logit link is logistic regression.

## Open items
- The chapter does not show the Poisson likelihood or the log-link estimation. A one-line statement of the Poisson mean-variance relationship would help.
- The chapter points to a link-functions chapter for the common choices. The cross-reference should be checked when that chapter is reviewed.
