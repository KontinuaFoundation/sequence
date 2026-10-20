# Least Squares — Notes

## Summary
Defines the sum of squared errors S(b₀, b₁), derives the least squares slope b₁ = S_xy / S_xx and intercept b₀ = ȳ − b₁x̄ with calculus, works the five-point example (b = (0.05, 1.99), SS_res = 0.107), shows the matrix form Xᵀ Xb = Xᵀy, and discusses outliers. It has three exercises: a four-point line (ŷ = 0.7 + 2.2x), a prediction with SS_res = 1.80, and a conceptual question about squaring.

## Changes in this pass
- Added a high school example (hours studied versus test score) to the opening.

## Checked and correct
- Five-point example: Σy = 30.1, Σxy = 110.2, S_xy = 19.9, S_xx = 10, b₁ = 1.99, b₀ = 0.05.
- Residuals 0.06, −0.13, 0.18, −0.21, 0.10 give SS_res = 0.107.
- Matrix form: XᵀX = [[5, 15], [15, 55]], Xᵀy = (30.1, 110.2), and the solution (0.05, 1.99).
- Four-point exercise: x̄ = 1.5, ȳ = 4, S_xx = 5, S_xy = 11, b₁ = 2.2, b₀ = 0.7.
- Prediction at x = 4 is 9.5, the residuals are 0.3, 0.1, −1.1, 0.7, and SS_res = 1.80.

## Open items
- The worked example says the fit "matches the fitted line from the previous chapter." The simple linear regression chapter was not reopened in this pass, so the match is unverified there.
- The section on robust methods names no method. A one-sentence pointer (for example, to least absolute deviations) would help.
