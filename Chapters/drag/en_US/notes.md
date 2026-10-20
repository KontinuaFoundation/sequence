# Drag — Notes

## Summary
Uses the history of artillery calculations to introduce quadratic wind resistance (F = μ|v|²), resolves the launch velocity into components, sets up Newton's second law with gravity and drag, simulates a 45 kg shell in Python, and finds terminal velocity (≈94 m/s for the example, which checks out: √(441/0.05)).

## Strengths
- The wind-tunnel example makes the v² dependence intuitive (three times the molecules, each hitting three times harder).
- The terminal velocity exercise is correct and ties to the kinematic equations no longer applying.
- The simulation is a realistic extension of the falling-bodies work.

## Weaknesses
- **Python indentation:** after `import numpy as np`, every line is indented four spaces, which raises an IndentationError. The first line is not indented.
- **Wrong drag direction:** `force = force_of_gravity - wind_resistance * velocity**2` squares each component and keeps its sign, so drag points in the wrong direction when the shell moves left or down. It should be −μ|v| v (magnitude μ|v|², opposite to v).
- **Unverified output:** the printed result (1696.70 m at 20.73 s) comes from the buggy force line and should be recomputed.
- **Unfinished:** a FIXME asks whether the section is finished ("odd stopping point"), and terminal velocity has a FIXME to expand.
- **Notation:** the shell's mass is written as b in the force formula and as m elsewhere.

## Index entries added
drag!quadratic, plus the existing wind resistance and terminal velocity entries kept.

## Editor to-do
- Fix the Python indentation and the drag direction, then rerun for the printed numbers.
- Finish the section and unify the mass symbol.
