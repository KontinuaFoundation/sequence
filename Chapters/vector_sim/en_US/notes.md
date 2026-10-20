# Simulation with Vectors — Notes

## Summary
Builds a 2D two-moon gravity simulation with numpy vectors and a fixed time step: text output, matplotlib paths with time markers, a center-of-mass frame, an animation with velocity and acceleration arrows, and a three-body extension.

## Strengths
- The printed positions match the code: after one 2-hour step, Moon 1 is at (720,000, 200,180,000) and Moon 2 at (−324,000, −149,985,600), which I recomputed.
- The data-point count (1,201 for 100 days at 2-hour steps) is correct.
- The conservation-of-momentum section (center of mass) is a clear physical check.

## Weaknesses
- **Wrong comment:** the animation sets `MAX_TIME = 400 * SEC_PER_DAY` with a comment "# 100 days".
- **Collision logic:** the animation prints "Collided" but does not stop, unlike the text version, which breaks out of the loop.
- **Constant name:** the text says "g is the universal gravitational constant" but the code uses G.
- **Notation:** v_t = v_0 + (t/m)F uses t as a duration, while the step-size section uses t for time.
- **Overstatement:** "And no one has" should specify a general closed-form solution.

## Index entries added
step size, simulation!text-based, NumPy array, momentum!conservation of, center of mass, animation!matplotlib, dynamical systems, chaos theory.

## Editor to-do
- Fix the MAX_TIME comment and the "g" versus "G" notation.
- Make the animation stop on collision (or say it does not).

