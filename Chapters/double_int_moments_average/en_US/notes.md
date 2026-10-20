# Moments, Surface Area, and Average Value — Notes

## Summary
Covers moments of inertia (I_x, I_y, I_o), radii of gyration, the surface-area formula ∬√(1 + f_x² + f_y²) dA with worked examples (the triangle under z = 2 − y², area (1/16)(65^{3/2} − 1) ≈ 32.69), and average values of two-variable functions. There are exercises for each section, with answers.

## Changes in this pass
- Moment exercise 1 (ρ = xy over [1,4] × [0,3]): the arithmetic was wrong. I_x = 1215/8 (not 1215/2), m = 135/4 (not 135/2), and ȳ̄² = 9/2, so ȳ̄ = 3/√2 (not 3).
- Moment exercise 2: the statement had ρ = x, which makes the total mass 0 (x cos x is odd on [−π/2, π/2]), so the radius of gyration is undefined. The worked answer was for ρ = y. The statement now uses ρ = y, and the answer √(π²/12 − 1/2) stands.
- Moment exercise 3: the formula R = √(x̄̄² + ȳ̄²) was misapplied. R is the radius of gyration about the origin, so R = √(93/35).
- The worked disk example had the wrong variable limits in the I_y step (θ instead of r). It now reads r = 0 to 4 sin θ.
- Surface-area example: "{3}{4}y" → "\frac{3}{4}y".
- Average-value exercise 1 (x sin y over [0,2] × [−π/2, π/2]): the answer used [0, π] for y and gave 2/π. Over the stated region, the average is 0, since sin y is odd on the symmetric interval. Answer rewritten.
- Average-value exercise 2: the integral had ∫_{π/2}^{π/2}; it is now ∫_{−π/2}^{π/2}.
- Fixed "−pi/2" to "−\pi/2" in the moment answer.

## Checked and correct
- I_x = ρr⁴/12 for a centered square; I_o = πa⁴b/2 = ½MR² for the disk.
- The disk with ρ = y (radius 2, centered at (0, 2)): m = 8π, I_y = 8π, x̄̄ = 1.
- Half-annulus with ρ = r (1 ≤ r ≤ 2, 0 ≤ θ ≤ π): I_o = 31π/5, m = 7π/3, R² = 93/35.
- Triangle surface area under z = 2 − y²: (1/16)(65^{3/2} − 1) ≈ 32.69.
- Plane surface area 12√14, paraboloid cap ≈ 539.2, cylinder-cut saddle ≈ 52.14.
- Average values: 0 for the rectangle example, 1 for the circle with x + y, and 1 for the triangle with xy.

## Open items
- The I_y worked example in the disk-with-density-y section has a long chain of trig identities (lines around the "64/5" step). The final value 8π is correct, but the middle steps were not re-derived in this pass.
- The surface-area derivation writes [f_x(x, y)]² where it should be evaluated at (x_i, y_j). This is a notational point only.
- The surface-area section still has long TikZ figures that were not checked.
