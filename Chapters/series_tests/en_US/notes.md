# Convergence Tests for Series — Notes

## Summary
Covers the Test for Divergence, the Integral Test (with the bounds on the remainder and the 123-term example), the Direct and Limit Comparison Tests, and the worked p-series and comparison examples. The chapter has exercises for each test.

## Changes in this pass
- Integral test section: the series was written as Σ1/2ⁱ when the examples use 1/i². The figures' axis labels and captions now match 1/i².
- Corrected the bound for Σ1/i². The rectangles lie below the curve, so Σ_{i≥2} 1/i² < ∫_1^∞ 1/x² dx. The old bound used ∫_0^∞, which diverges and is not useful.
- Changed the √x series to √i, and the index on the 1/(n²+1) example to n.
- Corrected the integral in the 5/(3x−1) answer. The antiderivative is (5/3)ln(3x−1), so the lower limit gives ln 2, not ln 4.
- Corrected the remainder derivation. The tail is a_{n+1} + a_{n+2} + ..., not a_{n−1} + a_{n−2} + ....
- Remainder exercise: the answer's bounds now use the integrals from 11 and 10 to match s₁₀.
- Comparison example 9^n/(3 + 10^n): reversed the inequality. The old version claimed (9/10)^n < 9^n/(3+10^n), which is false. The correct bound is 9^n/(3+10^n) < (9/10)^n.
- Typos: "have already determine," "Which implies," "Subsequently," and the `\textbf{Example}` spacing.

## Checked and correct
- The 10th partial sum (3.593) and the bound 3/200 = 0.015 for Σ3/n³.
- The n = 123 count for error 0.0001.
- s₁₀ for 1/n⁴ (1.082037), the bounds 1.082287 to 1.082370, and n = 33 for error 0.00001.
- The p-series answers and the limit comparison of √(n³+1)/(3n³+4n²+2), which gives 1/3.

## Open items
- The Integral Test example ends with "The first 5 terms" figures, which may need a caption check against the figure labels.
- The Limit Comparison Test paragraph ends with a stray "\\" after "the following:".
- The comparison figure (fig:compare1) reads "Σ 1/(3^n+3)" in the legend where the caption says "< Σ 1/3^n" for all n. The blue partial sums use 1/(3^n+3) correctly.
