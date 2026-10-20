# Vector-valued Functions — Notes

## Summary
Defines vector-valued functions with the hammer's flight, f(t) = [4t + 1, 6, z(t)], then differentiates component by component for velocity and acceleration, with 3D figures showing position, velocity, and acceleration vectors at t = 0, 1, and 2.

## Strengths
- The figures' values are consistent with a vertical term of −4.9t² (f(1) = 9.1, f(2) = 6.4, velocity [4, 0, 2.2] at t = 1).
- The landing time t ≈ 2.6056 (where z = 0) matches the figure domain.
- The component-wise differentiation and the constant acceleration [0, 0, −9.8] are clear.

## Weaknesses
- **Wrong coefficient:** the text gives z(t) = −4.8t² + 12t + 2, but the figures and the velocity −9.8t + 12 need −4.9t². With −4.8, f(1) = 9.2 and f(2) = 6.8, not 9.1 and 6.4.
- **Wrong chain:** "R → R² → R³" and "returns a 2-dimensional vector" conflict with the 3D position used in the rest of the chapter.
- **Leftover comment:** "% Format 12/ m2" is in the source.

## Index entries added
vector-valued function, position vector, velocity vector, acceleration vector, derivative!componentwise, vector!components, trajectory.

## Editor to-do
- Change the coefficient to −4.9 in the position formula.
- Fix the R → R² → R³ chain and the "2-dimensional" wording.

