# Applying Numerical Methods to Bivariate Data — Notes

## Summary
Moves from scatterplots to numbers: Pearson's r (range, sign for direction, cutoffs for strength), a linear regression model with residuals and the least-squares line (b = r·S_y/S_x, a = Ȳ − bX̄), interpretation of slope and intercept, and R² = r², then a worked 10-teacher example with Excel and Python. The numbers check out: the teacher summary statistics, r = 0.9957, b = 1.673, a = 30.20, and R² = 0.9915 all recompute.

## Strengths
- Each formula is followed by an interpretation, and the "on average" phrasing is explained.
- The 10-teacher example runs from summary statistics through residuals and R² in one thread.
- Excel and Python both produce the same values, which helps students check their work.

## Weaknesses
- **Empty exercise and answer:** "Interpreting a Computed r" has only "%Insert exercise" and "%Insert answer" placeholders.
- **Empty section:** "Review of Scatter Plots" has no content.
- **Rounding:** the Python output shows intercept 30.203, while the text uses 30.204 (from the rounded slope).

## Index entries added
correlation!direction, correlation!strength. (Existing entries kept.)

## Editor to-do
- Write the empty exercise and answer, or remove them.
- Remove the empty "Review of Scatter Plots" heading.
