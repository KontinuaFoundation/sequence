# Statistical Inferences for Means — Notes

## Summary
Introduces the t-distribution and its degrees of freedom, conditions for inference about a mean, matched pairs, the t-interval for one mean (streaming watch time: (43.75, 51.85) minutes), interpretation, the t-test for one mean, a two-sample t-interval and test with Welch degrees of freedom, procedure selection, and common errors. Ends with an Excel walkthrough.

## Changes in this pass
- Corrected the df = 100 critical value: 1.660 for 90% confidence (1.984 is the 95% value).
- Qualified the claim that a CI and test always agree: it holds for a two-sided test at α = 1 − confidence level.
- Fixed "TTesting" to "Testing."
- Clarified that the unpooled two-sample interval is the safe default, instead of asserting what the AP CED includes.

## Strengths
- All the worked intervals and tests are correct: t* values (2.064, 2.069, 2.602, 1.796, 1.699), the streaming interval, the bakery test (p ≈ 0.278), the streaming test (p ≈ 0.0465), the two-sample interval (−15.57, −3.23), and the store test (p ≈ 0.038).
- Interpretation of confidence (about the method, not the probability of μ) is correct.
- The Excel CONFIDENCE.T and T.INV.2T directions are correct.

## Open items
- The two-sample df values are Welch approximations; the text gives them as technology output. The example df ≈ 33 is consistent with the Welch formula.
- The flowchart comment in the source ("Verify cfigure environment") should be removed.
