# Change of Variables — Notes

## Summary
Transforms a normal distribution of ice-sphere radius into the distribution of mass via H(m) = F(g(m)), derives the density with the chain rule (with code), and then handles a decreasing transformation: the current I = 12/R for normally distributed resistance. It gives the density of the current, a worked probability (P(I > 0.6 A) ≈ 9.1%), and one exercise (P(I < 0.4 A) ≈ 2.3%).

## Changes in this pass
- Fixed the example radius. The mass 1.44 g belongs to the mean radius 0.7 cm. A 5 cm sphere has a mass of 523.6 g, and this is no longer mixed in with the mean.
- Fixed the median statement. The median radius is 0.7 cm, so the median mass is 1.44 g.
- Fixed g(m) to use m, not x, in the radius-from-mass formula.
- Fixed "then" to "than" in the sanity-check comment.
- Replaced the FIXME with the decreasing-function derivation. H(i) = 1 − F(g(i)), and the density is F′(g(i))|g′(i)|. The absolute value handles the sign of g′.
- Added the lightbulb density h(i) and a short Python function, which prints 6.383 at i = 0.5 A.
- Added a worked example (P(I > 0.6) = Φ(−4/3) ≈ 0.091) and an exercise (P(I < 0.4) ≈ 0.023).

## Checked and correct
- g′(m) = (1/3)(3/(4π))^{1/3} m^{−2/3} and the chain-rule derivation.
- Mass at r = 5 cm: 4π(125)/3 ≈ 523.6 g.
- The density at i = 0.5 A is 6.383. The density peaks near 0.49 A (checked numerically).

## Open items
- The first section's figures (before.png, cdf_after.png, pdf.png, and the others) are image files and were not checked here.
- The chapter does not have a high school link. The ice-sphere opening is a lab-like example, which may be enough.
