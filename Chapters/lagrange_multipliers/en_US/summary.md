# Lagrange Multipliers: Summary

## What the chapter covers
Teaches constrained optimization: maximize or minimize f(x, y) subject to g(x, y) = c. Two TikZ figures build the intuition: walking along the constraint, the best point is where it touches a level curve of f instead of crossing it, so ∇f and ∇g are parallel. Then it states the method ∇f = λ∇g, works a fence problem and a max/min on a circle, redoes the soda can (h = 2r, found before using the volume), finds the most likely spinner probabilities from observed counts (maximum likelihood), explains λ as a shadow price, and solves the equations with SymPy.

## Key ideas
- At a constrained extreme, the constraint curve is tangent to a level curve of f, so ∇f = λ∇g.
- Solve f_x = λg_x, f_y = λg_y, g = c; then compare f at every candidate.
- λ is how fast the optimum changes as the constraint value c changes.
- Maximum likelihood: with observed counts nᵢ, the most likely probabilities are nᵢ/N.

## Changes in this pass
- New chapter, placed in volume 20 right after gradients_optimization, whose gradients and level curves it builds on. It fills the gap noted in suggestions.md (gradients_optimization set up Lagrange multipliers but stopped short).
- Two TikZ intuition figures: level curves of xy with the constraint x + y = 8 (tangency at (4, 4)), and a close-up comparing ∇f and ∇g at the optimum and at a non-optimal point, with an arrow showing the uphill direction along the path.
- Probability example: the most likely spinner probabilities (0.5, 0.3, 0.2) from 10/6/4 spins. It explains independence and uses logs (volume 10), since probability is not formally taught until volume 28. An exercise shows that maximum entropy gives equal probabilities.
- Includes a SymPy listing (lagrange.py) with real output and 5 exercises with answers (circle, river fence with λ = 25, biggest box, ellipse, entropy).
- All values verified with SymPy and a numerical search.
