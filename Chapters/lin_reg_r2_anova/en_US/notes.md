# Evaluating the Fit of a Linear Regression Model — Notes

## Summary
Covers residuals and residual plots, the three sums of squares (SS_tot, SS_res, SS_reg), R² = 1 − SS_res/SS_tot (with R² = r² for simple regression), the example R² ≈ 0.997 for the quiz data, RMSE = √(SS_res/n) ≈ 0.146, and the limits of these measures. It has three exercises: computing R² = 0.75, showing R² = 0 for a model that predicts ȳ, and reading a curved residual plot.

## Changes in this pass
- Added a high school link: guessing a friend's quiz score with the class average explains nothing, so R² = 0.
- Renamed the third exercise from "Compare two residual plots" to "Read a residual plot." The exercise describes one plot.

## Checked and correct
- SS_tot = 39.708 for the quiz data (deviations from ȳ = 6.02 squared and summed).
- R² = 1 − 0.107/39.708 ≈ 0.997.
- RMSE = √(0.107/5) ≈ 0.146 points.
- Exercise answer: R² = 0.75 when SS_res = 25 and SS_tot = 100.

## Open items
- The file name and the section list mention ANOVA, but the chapter has no ANOVA content. Either add a short F-test section (the regression F statistic and its relation to R²), or rename the chapter.
- The chapter has one worked example (R² for the quiz data). A second worked example, such as computing RMSE and reading a residual plot, would match the standard format.
