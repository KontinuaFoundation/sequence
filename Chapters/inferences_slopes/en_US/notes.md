# Statistical Inferences for Slopes — Notes

## Summary
Builds the confidence interval for β₁ from LINEST or regression output (90% interval (−0.245, −0.085) for the sleep study), checks the LINER conditions with a residual plot, and runs a one-sided t-test (t = −4.01, p = 0.0035) with the rule for converting two-sided p-values. Includes Excel (LINEST, T.INV.2T, T.DIST) and Python (scipy.stats.linregress) walkthroughs.

## Changes in this pass
- Fixed a broken quotation in the Python note on one-sided p-values.

## Strengths
- The t* values (1.943 for df = 6 at 90%, 2.228 for df = 10 at 95%) and the margin and interval numbers are correct.
- The one-sided p-value rule (divide by 2 only when the sign of t matches H_a) is correct and carefully stated.
- The Excel and Python results match the hand calculations: t = −4.0131 and p = 0.0035.

## Open items
- The residual plot and dotplot in the conditions section are drawn by hand to show the pattern. They are illustrative and not computed from the eight residuals.
