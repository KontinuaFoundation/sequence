# Regression Basics for the Slope — Notes

## Summary
Introduces the population regression model Y = β₀ + β₁X + ε, the difference between parameters and statistics, the least-squares formulas b₁ = r·s_y/s_x and b₀ = ȳ − b₁x̄, and a sleep study with eight teenagers (b₁ = −0.165, b₀ = 8.25). Ends with a spreadsheet walkthrough (SLOPE, INTERCEPT, CORREL, STDEV.S).

## Changes in this pass
- Corrected s_y to 0.473 in the summary statistics. The old 0.47 rounded too far to reproduce b₁ = −0.165 from r = −0.854 (verified: S_xy = −6.925, S_xx = 42, S_yy = 1.567).

## Strengths
- All summary values are correct: x̄ = 5.5, ȳ ≈ 7.34, s_x = 2.45, s_y = 0.473, r = −0.854, b₁ = −0.165, b₀ = 8.25.
- The Excel results match the hand calculations: SLOPE = −0.1649, INTERCEPT = 8.2506, CORREL = −0.8536, and STDEV.S values 2.4495 and 0.4732.
- The distinction between parameters (β) and statistics (b) is clear.

## Open items
- The chapter ends after the spreadsheet walkthrough. The inference for the slope (the t-interval and test) is covered in the next chapter.
- Some exercises are commented out in the source (the spot-the-error and computing exercises). Decide whether to restore them.
