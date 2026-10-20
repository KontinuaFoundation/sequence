# Optimization — Notes

## Summary
Introduces optimization through critical points (f′ = 0), relative and absolute extrema, the Second Derivative Test, the closed interval method, a general strategy, worked examples (x² − 4x + 1, a cost function, a fenced enclosure with area 450), a summary table of tests, and a Python/SymPy script with exercises.

## Strengths
- The worked answers are correct: min −3 at x = 2 for x² − 4x + 1; min −4 at x = 3 for x² − 6x + 5; minimum cost $28 at 6 units; max area 450 at 30 × 15.
- The closed-interval figure (f(x) = x³ − 6x² + 9x + 1 on [0.5, 4.25]) is consistent with its caption.
- The Python exercise progression (20x − x², then x³ with an inconclusive test) teaches the second derivative test well.

## Weaknesses
- **Wrong table row:** for points where f′ does not exist, the table says to run the second derivative test. That test needs f′(c) = 0, so it cannot be used there. Use the first-derivative (sign-change) test instead.
- **Imprecise claim:** "This is when the second derivative of the point is also equal to zero" implies all such points are inflection points. Only some are (for example, x³ at 0; not x² at 0).
- **Open FIXME:** a note asks to add Python for absolute extrema and the derivative test.
- **Leftover source:** a commented-out standard-form section (lines 67–105) remains in the file.

## Index entries added
objective function, closed interval method, optimization!general strategy, inflection point, optimization!word problems, optimization!enclosure problem, optimization!cost minimization.

## Editor to-do
- Fix the undefined-derivative row and the inflection-point sentence.
- Finish the Python FIXME and remove or restore the commented-out section.

