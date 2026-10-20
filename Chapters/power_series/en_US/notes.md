# Power Series — Notes

## Summary
Introduces power series from 1/(1−x), builds representations via partial fractions, applies the ratio and root tests to find radius and interval of convergence, works Bessel-function and alternating examples, and uses term-by-term differentiation and integration (1/(1−x)², ln(1+x), and arctan x). Includes exercises.

## Changes in this pass
- Corrected the term-by-term derivative. The derivative of Σ c_n(x−a)ⁿ is Σ n·c_n(x−a)^{n−1}, not Σ c_n(x−a)^{n−1}.
- Corrected the integral series. The sum of the integrals now has a "+" before the c_n/(n+1) term.
- Fixed the index in 1/(1−x) = Σ xⁿ. It starts at n = 0, not n = 1 (in the 1/(1−x)² example).
- Fixed the ln(1+x) derivation. The old line "d/dx 1/(1−x) = ln(1−x)" was false. It now cites d/dx ln(1+x) = 1/(1+x).
- Fixed the x = 1 endpoint of the radius example. The series starts at n = 0.
- Fixed the interval endpoint typo [a−R, a+r] to [a−R, a+R].
- Fixed the Bessel working: (n = 1)! is now (n + 1)!, and a missing backslash on \frac and \lim.
- Fixed the arctan answer, where "sum" lacked a backslash.
- Typos: "do not exist," "partials sums."
- The ratio example for n!xⁿ says the limit is 0 when x = 0. This is left as written.

## Checked and correct
- The partial-fraction decomposition (2x−4)/(x²−4x+3) = 1/(x−1) + 1/(x−3) and the power series for each part.
- The interval (−1/3, 1/3] for Σ(−3)ⁿxⁿ/√(n+1). The endpoint −1/3 diverges (p = 1/2) and 1/3 converges (alternating).
- The Bessel result (convergent for all x).
- The root test radius √3 and the alternating series interval [−1, 1].
- The ln(1+x) series with C = 0, and the arctan series.

## Open items
- No high school link yet. A possible example: calculators approximate functions like sin x with polynomials.
- The partial fraction example says "the process is left as an exercise for the student." This is a placeholder. Either add a line of work or keep it short.
