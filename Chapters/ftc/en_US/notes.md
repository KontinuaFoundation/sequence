# The Fundamental Theorem of Calculus — Notes

## Summary
States and proves the two parts of the FTC, gives the Fresnel and chain-rule examples, practices FTC derivatives, evaluates the household energy integral (26.5 kWh), works AP-style exercises, and covers average value, position-velocity-acceleration relationships, and a velocity-from-force exercise.

## Changes in this pass
- Fixed the AP limit answer: the limit uses g(1)/g′(1) = 2, not g(6)/g′(6).
- Fixed the Fresnel derivative: S′(x) = sin(πx²/2), not sin(πt²/2).
- Made the chain-rule example use a consistent lower limit (1) in both the setup and the derivative.
- Fixed a missing minus sign in the FTC practice answer for ∫_{√x}^{π/4}, which now gives −½ tan √x.
- Fixed the frac typo in the defint6 answer (\frac).
- Relabeled the power-consumption axis from kW to W, to match the values.
- Replaced two empty subsections (work, impulse) with a short paragraph pointing to the definite-integral chapter.

## Strengths
- The energy integral is correct: ∫₀²⁴ (1/10)t²(t − 24)² dt = 26,542 Wh ≈ 26.5 kWh.
- The AP-style answers are correct: h(6) < h′(6) < h″(6) (defint 3, the FTC3 ranking), f(−5) = 2π − 2 (defint6), and v(3) ≈ 11.71 (defint7).
- The average value of 3 + x² on [−2, 1] is 4, and the average of √cos x on [0, π/2] is about 0.763.

## Open items
- The proof in the FTC section uses "min and max on (a, b)" where it should use the subinterval [x, x + h]. The argument is still valid, but the wording is loose.
- The FIXME comments about the chain-rule and area-between-curves sections remain in the source.
