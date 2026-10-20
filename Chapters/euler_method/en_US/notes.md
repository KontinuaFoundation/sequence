# Euler's Method — Notes

## Summary
Builds Euler's method from linear approximations of dy/dx = x + y, gives the update formula y_n = y_{n−1} + h·F(x_{n−1}, y_{n−1}), and works three examples: a 0.2-step table for dy/dx = 2x + y, the 2012 AP BC problem (7/4), an RC-circuit charge problem (2.77 C), and the 2012 AP free-response problem (19).

## Strengths
- The step-size comparison (first approximation, step 0.5, step 0.25) is correct at each point.
- Each table entry in the 0.2-step example is correct through y₅ = 3.46496.
- The circuit answer is correct: Q′ = 12 − 4Q gives Q(0.5) ≈ 2.7667, which rounds to 2.77 C.
- The two AP problems give 7/4 and 19, matching the official approaches.

## Weaknesses
- **Wrong final value:** the text gives y(1) ≈ 3.4696, but the table's y₅ is 3.46496.
- **Wrong x value:** "Suppose we stop the first approximation at x = 1.5" should be x = 0.5, as the next sentence uses.
- **Notation:** the circuit working writes dQ/dT and "the unit it is Coulombs."
- **Unverified cross-reference:** the circuit exercise says "the previous chapter on slope fields" discussed inductors. The slope-fields chapter has not been checked against this.

## Index entries added
slope field, step size, initial value problem, Kirchhoff's law, RC circuit. The chapter already had Euler's method.

## Editor to-do
- Fix y(1) ≈ 3.4696 and the x = 1.5 typo.
- Check the slope-fields cross-reference and the dQ/dT notation.
