# Projections — Notes

## Summary
Introduces the projection of u onto v as a component along v plus an orthogonal component, gives the formula proj_v(u) = (u·v)/(v·v) v with a 3D example and a 2D exercise, and shows the Python version.

## Strengths
- The worked example is correct: proj of (1, 4, 6) onto (−2, 6, 2) is (34/44)(−2, 6, 2) ≈ (−1.545, 4.636, 1.545).
- The formula and the note that the vector v cannot be cancelled are stated correctly.
- The Python snippet matches the formula.

## Weaknesses
- **Reversed statement:** "To calculate the projection of v onto u, use this formula" should say u onto v.
- **Exercise rounding:** the answer gives (−1.076, 1.61); the exact value is (−1.077, 1.615).
- **Placement:** a comment at the top says the chapter feels out of place and might merge into transformations (left in the source).

## Index entries added
projection!orthogonal component, projection!example, projection!Python, projection!shadow analogy, projection!beyond the vector, vector!projection.

## Editor to-do
- Fix the u/v reversal and the exercise rounding.
- Decide whether to merge this chapter into transformations.
