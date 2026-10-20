# Random Variables and Expected Value — Notes

## Summary
Defines discrete random variables and PMFs, expected value, variance, linearity of expectation, and a game example. Then extends mean to continuous PDFs (transaction times, the exponential mean), works a COVID onset-time exercise, and computes expected values for two-variable joint densities.

## Changes in this pass
- Changed the transaction-time domain from 0–2 seconds to 0–250 milliseconds, to match the figure (mean 160 on the 0–250 axis).
- Replaced the messy intermediate arithmetic in the COVID onset answer with a clean antiderivative and closed form: μ = (6250 − 108250·e^{−4.8})/119 ≈ 45.04 hours.
- Fixed the e^{−∞} macro in the two-variable answer.

## Strengths
- The die and coin computations are correct: E = 7/2 and Var = 35/12 for one die; E = 1 and Var = 1/2 for two coins; two-dice sum Var = 35/6.
- The game example (−$2.50 per game) and the exercise answers are correct.
- The two-variable example gives μ_x = 5 and μ_y = 2, and the exercise gives 7/12 and 4/3. All are correct.

## Open items
- The COVID answer's closed form was verified numerically (≈45.035), not by re-deriving every step in the text.
- The "Expected Value/Mean" section repeats the definition from the first section. It could be shortened.
