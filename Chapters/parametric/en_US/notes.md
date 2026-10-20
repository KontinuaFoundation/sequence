# Parametric Functions — Notes

## Summary
Introduces x(t) and y(t), eliminates the parameter to get rectangular form (line and unit circle), sketches parametric curves with a table and direction of motion, provides a Python animation, then covers derivatives dy/dx = (dy/dt)/(dx/dt), speed, and arc length.

## Strengths
- The rectangular-form conversions are correct: 2t + 1 and 3t − 4 give y = (3/2)x − 11/2, and cos t, sin t give x² + y² = 1.
- The sketch tables are correct, including the parabola (x = t + 1, y = t²) and the 4 − 2t, 3 + 6t − 4t² exercise.
- The parametric3 answers (horizontal tangent at (0, 0), vertical tangents at (−2, 1) and (2, 1)) and the circle arc length 2π are correct.
- The speed example evaluates to about 12.3 at t = 2 (√(12² + 2.72²) ≈ 12.30).

## Weaknesses
- **Incomplete derivation:** the check for dy/dx = 3/(2t) uses t = √(x − 1), which holds only for t ≥ 0. For t < 0 the sign flips.
- **Missing context:** "approximately 12.3 cm/s" gives units but no setup (the problem's x(t) and y(t) are not stated).
- **FIXMEs:** "Sketched example" and "Expand on section" for arc length are open.
- **Dependency:** the animation saves an .mp4, which needs ffmpeg installed. The text does not say so.

## Index entries added
parametric equations, eliminating the parameter, parametric curve!sketching, Archimedean spiral, speed!of a parametric curve, arc length!parametric, derivative!parametric.

## Editor to-do
- State the t ≥ 0 restriction or derive dy/dx without substitution.
- Give the setup for the 12.3 example and mention ffmpeg.
- Resolve the two FIXMEs.

