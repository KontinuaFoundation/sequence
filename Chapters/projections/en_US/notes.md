# Projections — Notes

## Summary
Introduces the projection of u onto v as a component along v plus an orthogonal component, gives the formula proj_v(u) = (u·v)/(v·v) v with a 3D worked example and two exercises, and shows the Python version.

## Changes in this pass
- Fixed "projection of v onto u" to "projection of u onto v" in the formula section.
- Gave the 2D exercise's answer exactly: (−14/13, 21/13) ≈ (−1.077, 1.615). The old value was rounded wrong.
- Removed the stray "1*-4" notation, and fixed a missing bracket in the 3D worked example.
- Labeled the 3D example as a worked example, and added an unworked exercise (projection of (3, 4) onto (1, 0), with the orthogonal component (0, 4)).

## Strengths
- The 3D worked example is correct: proj of (1, 4, 6) onto (−2, 6, 2) is (34/44)(−2, 6, 2) ≈ (−1.545, 4.636, 1.545).
- The formula and the note that the vector v cannot be cancelled are correct.
- The Python snippet matches the formula.

## Open items
- A comment at the top of the file says the chapter feels out of place and might merge into transformations. The comment is still there. Decide on the placement.
