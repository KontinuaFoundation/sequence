# Mass, Charge, and Center of Mass — Notes

## Summary
Defines mass and charge as double integrals of a density over a lamina (126 for ρ = 3y² over a rectangle; 5/24 C for σ = xy over a triangle), then center of mass (x̄, ȳ) = (1/m)∬(x or y)ρ dA. Worked examples: a triangle with ρ = 2 + x + 3y (x̄ = 15/22, ȳ = 4/11), and exercises for a half-arch with ρ = x (π − 4/π, π/4), a rectangle with ρ = 1 + x² + y² (mass 112, centroid (18/7, 195/112)), and a triangle with ρ = x + y (mass 6, centroid (3/4, 3/2)).

## Changes in this pass
- Fixed the outer limit in the triangle total-mass answer. It is ∫₀² (not ∫₀³), which matches the region 0 ≤ x ≤ 2 and the final value 6.
- Removed a stale FIXME comment about "reversed coordinates." The worked c.o.m. example uses x̄ = (1/m)∬x ρ dA with the right integrand, so the comment was wrong.
- Fixed a typo in the half-arch answer ("x − 0" → "x = 0").

## Checked and correct
- Total mass 126 for ρ = 3y² over [1,3] × [1,4].
- Mass 112 and the 18/7 and 195/112 centroid for ρ = 1 + x² + y² over [0,4] × [0,3].
- Mass 6 and centroid (3/4, 3/2) for the triangle with ρ = x + y.
- Charge 5/24 C for σ = xy over the triangle with vertices (0,1), (1,0), (1,1).
- Worked c.o.m. example: mass 11/3, x̄ = 15/22, ȳ = 4/11.
- Half-arch exercise: mass 2π, x̄ = π − 4/π, ȳ = π/4.

## Open items
- The charge figure is drawn at 3× scale (the triangle has corners (3,0), (3,3), (0,3)). The labels match the region, but the scale is not stated.
- The density-examples paragraph lists "animals per acre of forest" and "people per city block." These are examples of density, not of a lamina, so the sentence could be clearer.
- The worked triangle example uses a type I description. A brief note on why type I is easier could help students.
