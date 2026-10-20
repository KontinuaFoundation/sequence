# Trigonometric Functions — Notes

## Summary
Defines sine and cosine on the unit circle, shows their graphs, has students plot cosine in Python, and states derivatives and integrals of sine and cosine (with a limit-definition proof of d/dx cos x = −sin x). It closes with a spring-and-skate simulation that shows simple harmonic motion, and a short integral exercise.

## Strengths
- The unit-circle figures (sin 4π/3, cos 4π/3) tie the definitions to a concrete angle.
- Students write and run a plot in Python.
- The spring simulation links calculus (a ∝ −x) to a physical system.

## Weaknesses
- **Algebra error:** in trig derivative exercise 2, d/dx[sin x/(1 + cos x)] = 1/(1 + cos x), not 2/(1 + cos x)².
- **Simulation error:** spring_constant = −1 with mass = 100 gives ω = 0.1 rad/s, so the displacement will not track cos(t) over 8 s. Use k/m = 1 (for example, mass = 1 with k = −1), or say what the plot should show.
- **Unit mismatch:** the text says spring rate is 5 N/m; the code uses −1 N/m.
- **Typo:** "$cos(\theta)$" appears without a backslash in the derivatives paragraph.
- **Unfinished:** a FIXME for the spring diagram (FIXME: diagram).

## Index entries added
sine, cosine, unit circle, Pythagorean identity, derivatives of trigonometric functions, spring rate, simple harmonic motion, integrals of trigonometric functions. (Index was empty.)

## Editor to-do
- Fix the d/dx sin/(1+cos) answer and the spring constant.
- Add the spring diagram.
