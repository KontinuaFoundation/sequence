# Series — Notes

## Summary
Defines series and partial sums (s₄ = −75/256 for (−3/4)ⁱ), reindexing rules with a worked shift, convergence of Σi (divergent) and Σ1/2ⁱ (converges to 1), the harmonic-series divergence proof, geometric series (a/(1−r)) with a bouncing-ball example and exercises, p-series, Euler's sums, and the alternating series test with exercises.

## Changes in this pass
- Corrected two alternating-series answers. alt1 (1) claimed convergence, but the terms tend to 3/4, not 0, so the series diverges. alt1 (3) claimed convergence, but e^{2/n} tends to 1, so that series also diverges.
- Corrected the algebra in alt1 (2). The expansion dropped the constant terms of (n+1)² and the +1 in (n+1)³ + 1. The comparison reduces to 0 < n⁴ + 2n³ + n² − 2n − 1, which holds for n ≥ 1.
- Added the missing a_n to the Test for Divergence and to the convergence property.
- Fixed the geometric-series captions. The series diverge for r ≥ 1 and for r ≤ −1, not for r ≤ 1.
- Fixed the reindexing caption, which had a broken middle term. It now reads Σ 1/(n−1) for n from 2.
- Changed the harmonic bound to n ≥ 1 and added the limit step to the alternating-series example.
- Added a bouncing-ball example (total 3 m) as a high school link to geometric series.
- Fixed typos: "Example" colon, "Let us rewrite" sentence break.

## Strengths
- The partial sum, reindexing, and harmonic-series arguments are correct.
- Geometric sums are correct: 3/2, 20, 8/3, 1/7, and c = 3/2.
- The Euler-sum answers are correct.

## Open items
- The alt1 (1) answer still shows the algebra for a decreasing sequence before the divergence conclusion. The algebra is correct, but the answer could be shortened.
- The reindexing figure has a FIXME about moving the axis label.
