# Taylor and Maclaurin Series — Notes

## Summary
Derives c_n = f⁽ⁿ⁾(a)/n! by matching derivatives, states the Taylor and Maclaurin series, and works e^x (radius ∞), the Maclaurin series for sin x, cos x (derived by differentiating sin), and tan x (by dividing series). It also covers arctan, the binomial series with its radius of convergence, the series for ln(3/2), and the 2012 AP problems.

## Changes in this pass
- Fixed the general derivative formulas. The f'' and f''' lines had garbled text ("· + sn", "c\dot 4") and now read n(n−1)c_n(x−a)^{n−2} and 2·3·4 c_4(x−a).
- Corrected the n-th Taylor polynomial. The sum index now runs over i with f⁽ⁱ⁾(a), and for e^x it is a finite sum to n.
- Fixed the binomial table (stray \\ and k(k−1)(k−1) → k(k−1)).
- Fixed the 3rd-degree Taylor answer. The question asks for f(3.4), but the answer computed f(3.5). It now substitutes x = 3.4 and gets 2 − 0.4 + 0.48 + 0.128 = 2.208.
- Fixed "they 3rd-degree" to "the 3rd-degree" and a missing space after "Solution:."

## Checked and correct
- The Maclaurin series for sin x and cos x, and the tan x expansion x + x³/3 + 2x⁵/15 + 17x⁷/315.
- The radius of convergence of e^x (∞) and of the binomial series (1).
- The sum of Σ(−1)^{n−1}/(n 2ⁿ) = ln(3/2).
- The 2012 AP answers: 4/7 for Σ(−x/4)ⁿ at x = 3, 19.8 for the second-degree estimate at 1.4, and (C) for the cosine-type series.

## Open items
- No high school link. The e^x or sin x approximation could be tied to a calculator computing functions with polynomials.
- Notation: the tan x answer uses "$\frac{d}{dx}$" conventions inconsistently with other chapters. This is a style issue only.
- The tan x plot uses "tan(deg(x))" with domain ±1.47, which is only a plotting choice.
