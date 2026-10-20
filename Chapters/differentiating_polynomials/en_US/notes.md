# Differentiating Polynomials — Notes

## Summary
Defines differentiation through the three polynomial rules (sum, constant, power), works a quadcopter height-to-velocity example and a tangent-line figure (slope 13 at t = 2), gives a Python derivative_of_polynomial function, and covers second derivatives and acceleration with a motion exercise.

## Strengths
- The quadcopter example and the tangent-line figure (slope 13 at t = 2) are consistent with h'(t) = 6t² − 10t + 9.
- The motion exercise answers are correct (v = 4t³ − 6t² + 2t − 1, a = 12t² − 12t + 2, v(1.5) = 2, a(1.5) = 11).
- The Python derivative code gives 9x² + 2 for 3x³ + 2x + 5 and 0 for a constant, as the exercise says.

## Weaknesses
- **Wrong answer:** the derivative of 2t³ − 3t² − 4t is 6t² − 6t − 4. The printed answer has 3t² − 6t − 4.
- **Wrong factorization:** 49 − 16x⁶ = (7 + 4x³)(7 − 4x³). The printed answer has (7 + 4x³)(7 + 4³).
- **Unused variable:** derivative_of_polynomial computes degree_of_derivative but never uses it.
- **Stray text:** "We ignore the other solution ... because it is usual for time to start at zero" is a claim, not a reason. Rewrite as a convention of the problem.
- **Notation mix:** the second-derivative formula uses x while the rest of the chapter uses t.

## Index entries added
differentiation, prime notation, tangent line, acceleration, derivative!second, product rule, derivative!higher order.

## Editor to-do
- Correct the derivative of 2t³ − 3t² − 4t and the factorization of 49 − 16x⁶.
- Remove the unused variable and fix the x/t notation.

