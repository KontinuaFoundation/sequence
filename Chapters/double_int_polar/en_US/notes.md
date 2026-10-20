# Double Integrals in Other Coordinate Systems — Notes

## Summary
Derives the polar form of a double integral: the area of a polar subrectangle is r* Δr Δθ, so ∬f dA = ∫∫ f(r cos θ, r sin θ) r dr dθ. It works one example (x²y over a semicircle, 1250/3), three exercises converting to polar (e^{−x²−y²} over a quarter disk, xy² over a wedge, and √(x²+y²) over a circle), a volume under z = 4 − x² − y² (8π), and a pool volume (2600π cubic feet), with answers.

## Changes in this pass
- Fixed the midpoint formula. It read r_i* − ½(r_{i−1} + r_i); it is now an equals sign.
- Fixed δθ and δA_i to Δθ and ΔA_i in the area derivation.
- Removed the broken "(see figure ...)" placeholder.
- Fixed the TikZ curves that had an unclosed parenthesis in sqrt(1−x²).
- Fixed a stray "$" in the pool answer ("\textit{D}$ =").

## Checked and correct
- x²y over the semicircle of radius 5 (0 ≤ r ≤ 5, 0 ≤ θ ≤ π): 1250/3.
- Quarter-disk exponential: (π/4)(1 − e^{−4}).
- Wedge integral xy² over 0 ≤ θ ≤ π/6, 0 ≤ r ≤ 1: 1/120.
- Circle integral √(x²+y²) over r ≤ 2cos θ: 16/9.
- Volume under z = 4 − r²: 8π.
- Pool: depth z = 13/2 + 7x/40 over a 20-ft radius circle; volume 2600π cubic feet.

## Open items
- The semicircle figure uses a plain sqrt-based fill with no axis labels for r. It was not reviewed further.
- The volume exercise uses a 3D plot. The plot was not rendered or checked.
- The pool exercise is a good high school example. The answer uses the linear depth formula directly; it could explain where 7/40 and 13/2 come from in more detail.
