# Simple Linear Regression — Notes

## Summary
Introduces simple linear regression with the study-hours and quiz-score data: the model ŷ = b₀ + b₁x and the population model with an error term, least squares formulas b₁ = S_xy/S_xx and b₀ = ȳ − b₁x̄, the fitted line ŷ = 0.05 + 1.99x, a warning about predicting outside the data, and an interpretation of the slope that stops short of causation. It has three exercises (prediction, residual, and why the intercept is not useful).

## Changes in this pass
- Reworded the quiz scale to "out of 10 points on a quiz." The arithmetic was already correct.

## Checked and correct
- S_xx = 10, S_xy = 19.9, b₁ = 1.99, b₀ = 0.05.
- Prediction at 6 hours: 11.99 (and 6 is just outside the data range 1 to 5).
- Residuals 0.06, −0.13, 0.18, −0.21, 0.10 (sum 0).
- Exercise answers: 8.01 for 4 hours, and a residual of 0.18 at 3 hours (6.2 − 6.02).

## Open items
- The chapter has one fully worked example (the five-point fit) and a worked residual in the exercises. A second worked example, such as the residual at x = 5 with the full computation, would match the standard format more closely.
