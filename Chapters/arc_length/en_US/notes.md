# Arc Lengths — Notes

## Summary
Derives the arc-length formula from inscribed polygons, extends it to parametric and vector-valued curves, applies it to a shell's path and to distance traveled by a block on a spring, and gives four practice exercises (curve-length integrals, reconstructing f from an arc-length function, a 3D rocket path, and a matching integral).

## Changes in this pass
- Fixed the vector-valued arc-length integral: it integrates with respect to t (it said dx).
- Fixed the shell's position function to use t (v₀ cos θ · t and v₀ sin θ · t − 4.9t²), and the angle symbol (30°).
- Replaced the distance-traveled method. The arc length of the position-time graph, ∫√(1 + v²) dt, is not the physical distance. Distance is ∫|v(t)| dt. For the block, that is about 0.307 m (the old value 3.019 m was wrong). The displacement stays −0.0229 m.
- Fixed the figure caption to match the corrected definition of distance.
- Corrected length2: f(x) = (2/9)(3x + 4)^{3/2} + 2/9, and the point on f is (1.159, 4.766).

## Strengths
- The displacement of the block (−0.0229 m) is correct.
- The length1 integrals are all correct, including the tan form for y = ln(cos x).
- The 3D rocket answers are correct: about 84,745 m in the first 60 s and 84,898 m in the second 60 s.

## Open items
- The Archimedes bounds on π are given without a source. They are historically accepted values.
