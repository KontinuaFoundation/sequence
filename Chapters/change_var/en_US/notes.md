# Change of Variables — Notes

## Summary
Transforms a normal distribution of ice-sphere radius into the distribution of mass via H(m) = F(g(m)), derives the density with the chain rule, and begins a decreasing example (lightbulb current I = 12/R). The decreasing-case section is unfinished.

## Strengths
- The chain-rule derivation is correct: H′(m) = F′(g(m))g′(m).
- The code matches the math: g(m), the derivative, and the pdf-times-derivative all check out.
- The lightbulb setup is a good second example that shows a decreasing transformation.

## Weaknesses
- **Wrong example radius:** "a sphere has a radius of 5 cm, its mass is 4π(0.7³)/3 ≈ 1.44 g" mixes the 5 cm radius with the 0.7 cm mean. With r = 5 cm, the mass is 523.6 g.
- **Wrong reasoning:** "if half the balloons have a radius less than 5 cm" should refer to the median, which is 0.7 cm, giving a median mass of about 1.44 g.
- **Direction and variables:** "g(x) = 12/x is the function that will convert the current to resistance" is backwards, since g maps resistance to current. The derivative uses i and x interchangeably.
- **Unfinished section:** "FIXME finish this section with graphs and code." The lightbulb PDF is never derived.

## Index entries added
change of variables, change of variables (decreasing function), chain rule, cumulative distribution function (change of variables), probability density function (change of variables).

## Editor to-do
- Fix the 5 cm examples and the g direction, and use one variable name.
- Finish the decreasing-case section with the PDF, graph, and code.
