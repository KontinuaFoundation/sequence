# Power Series — Notes

## Summary
Introduces power series from 1/(1−x), builds representations via partial fractions, applies the ratio and root tests to find radius and interval of convergence, works Bessel-function and alternating examples, and uses term-by-term differentiation and integration (1/(1−x)², ln(1+x), and arctan x). Includes exercises.

## Strengths
- The partial-fraction representation of (2x−4)/(x²−4x+3) is correct: 1/(x−1) + 1/(x−3).
- The Bessel function convergence result (all x) and the 1/3-radius example with interval (−1/3, 1/3] are correct.
- The root-test exercise (radius √3) and the x-series exercise (interval [−1, 1]) are correct.
- The ln(1+x) and arctan x series are correct, and the constants of integration are computed.

## Weaknesses
- **Wrong derivative:** "d/dx [1/(1−x)] = ln(1−x)" is wrong. The correct antiderivative is −ln(1−x), since d/dx[−ln(1−x)] = 1/(1−x).
- **Index error:** 1/(1−x) = Σ_{n=1} xⁿ should start at n = 0.
- **Typos:** "[a−R, a+r]" should use R, "(n = 1)!" in the Bessel working should be (n + 1)!, "sum_" in the arctan answer lacks a backslash, and "convergent fort" should read "for."

## Index entries added
ratio test, root test, alternating series test, direct comparison test, partial fractions, Bessel function.

## Editor to-do
- Fix the ln(1−x) derivative and the Σ start index.
