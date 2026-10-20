# Python Lists — Notes

## Summary
Introduces Python lists with a favorites program, then uses a list of coefficients to represent and evaluate polynomials (evaluate_polynomial and polynomial_to_string), exercises for evaluation, and a matplotlib plot of x³ − 7x + 6 with its roots at −3, 1, and 2.

## Strengths
- The favorites program output matches the code exactly.
- The evaluation exercises are correct (16481.875 and 151.0), and the answer lists match the coefficient order.
- The plot observations are correct: y-intercept 6, and the roots −3, 1, and 2.
- The polynomial_to_string task list (skip zeros, omit x for degree 1, walk backwards) guides the student well.

## Weaknesses
- **Broken LaTeX:** `\pyfunction(join)` uses parentheses instead of braces, so it will not compile.
- **Output mismatch:** the sample output "1.0x**3 + 10.0x + -12.0" does not match the code, which prints `x^3` with a caret. The example also calls `pn1`, which contains a −3.0x² term, so it would print that term too. `pn_test` is defined but unused.
- **Shadowed built-in:** `sum` shadows Python's built-in name.
- **Typos:** "Polynomia 2" in the printed label; "crosses the y-axes" should be "x-axis" in the observations answer.
- **Wording:** the plotting steps say "two empty arrays," but the code uses lists.

## Index entries added
Python list, zero-based indexing, exponentiation, polynomial!evaluating, matplotlib, plotting polynomials, roots of a polynomial.

## Editor to-do
- Fix the `\pyfunction` macro, the sample output, and the `pn_test` call.
- Rename `sum` and correct "Polynomia" and the axis typo.

