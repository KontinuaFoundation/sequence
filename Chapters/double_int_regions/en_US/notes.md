# Double Integrals Over Non-Rectangular Regions — Notes

## Summary
Extends double integrals to regions D that sit inside a rectangle R. It defines type I and type II regions, shows how to tell which type a region is (vertical and horizontal line tests), and works two examples: ∬(2x + y) over the region between two parabolas (56/15), and ∬xy over the region bounded by y = x − 2 and x = y² (45/8, set up as type II). It ends with three exercises (e^{−y²}, x sin y, and (2x − y) over a disk), with answers.

## Changes in this pass
- Fixed the type II limits in the parabola-line example. The region lies between x = y² (on the left) and x = y + 2 (on the right), so the inner limits are y² to y + 2. The old limits were reversed and gave −45/8. The correct value is 45/8. The explanation of why type II avoids a split also now reads y² ≤ x ≤ y + 2.
- Fixed the type II definition: "h_1(y0 ≤ x" is now "h_1(y) ≤ x".
- Exercise 3 and its answer used different integrands, (2y − x) in the statement and (2x − y) in the work. The statement now uses (2x − y). The bounds were −3 ≤ x ≤ −3. They are now −3 ≤ x ≤ 3. The result is 0 (the integrand is odd in x and the disk is symmetric).
- Fixed "into to two parts" and "Solution:This" spacing.

## Checked and correct
- ∬(2x + y) dA over 3x² ≤ y ≤ 2 + x², −1 ≤ x ≤ 1: 56/15.
- Exercise 1: ∫₀³ 2y e^{−y²} dy = 1 − e^{−9} ≈ 0.9999.
- Exercise 2: 2 − (sin 4)/2 ≈ 2.378.
- The type I split for the line-and-parabola example (0 ≤ x ≤ 1 and 1 ≤ x ≤ 4).

## Open items
- The horizontal- and vertical-line figures are drawn with hand-typed coordinates. They were not checked against the curves.
- The section "Determining Region Type" has long TikZ blocks. They were not reviewed in this pass.
- This chapter has no high school link. A possible one is a garden bed bounded by a fence and a path.
