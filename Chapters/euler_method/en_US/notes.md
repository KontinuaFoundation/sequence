# Euler's Method — Notes

## Summary
Builds Euler's method from linear approximations of dy/dx = x + y, gives the update formula y_n = y_{n−1} + h·F(x_{n−1}, y_{n−1}), and works three examples: a 0.2-step table for dy/dx = 2x + y, the 2012 AP BC problem (7/4), and the 2012 AP free-response problem (19). It also has an RC-circuit charge exercise (2.77 C, exact value 2.59 C).

## Changes in this pass
- Fixed the final value of the 0.2-step example. It is y(1) ≈ 3.465 (the table gives 3.46496), not 3.4696. Added the exact solution 3e^x − 2x − 2 (y(1) ≈ 4.155) to show that the estimate is low.
- Fixed "stop the first approximation at x = 1.5" to x = 0.5, which is the point the next sentence uses.
- Corrected dQ/dT to dQ/dt and "the unit it Coulombs" to "the unit is coulombs."
- Added the exact solution Q(t) = 3(1 − e^{−4t}) for the circuit, so Q(0.5) ≈ 2.59 C. The Euler value is high because the charge curve bends downward.
- Added a speedometer analogy before the general description of the method.
- Replaced the display-math line in the opening with inline math.

## Strengths
- The step-size comparison (first approximation, step 0.5, step 0.25) is correct at each point.
- Every table entry in the 0.2-step example is correct.
- Both AP answers (7/4 and 19) are correct.

## Open items
- The circuit exercise refers to "the previous chapter on slope fields" for inductors. This cross-reference has not been checked against the slope-fields chapter.
- The circuit figure has no caption that says what it shows beyond "switch."
