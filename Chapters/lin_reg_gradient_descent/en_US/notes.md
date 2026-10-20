# Linear Regression and Gradient Descent — Notes

## Summary
Presents gradient descent as an alternative to the normal equations for linear regression: the mean squared error cost J(θ), its gradient (2/n)Xᵀ(Xθ − y), the update θ := θ − α∇J, and the effect of the learning rate. A worked step on the quiz data gives θ₁ = (0.1204, 0.4408) with α = 0.01, and an exercise takes the next step to θ₂ = (0.2119, 0.7774). It also explains why standardizing features helps convergence, and it ends with a question on large learning rates.

## Changes in this pass
- Added a high school link: walking down a hill in fog by feeling the slope.

## Checked and correct
- X^T y = (30.1, 110.2), and the first gradient is (−12.04, −44.08). So θ₁ = (0.1204, 0.4408).
- Exercise gd1: predictions (0.5612, 1.0020, 1.4428, 1.8836, 2.3244); residuals (−1.5388, −2.8980, −4.7572, −5.9164, −7.7756); the gradient is (−9.1544, −33.660); and θ₂ = (0.2119, 0.7774).
- The steps move toward the least squares solution (0.05, 1.99).

## Open items
- The chapter does not show how many steps are needed to reach the solution. A short table of several iterations would show the convergence.
- The gradient formula is written for the mean squared error with a 1/n factor; the factor 2/n in the gradient is correct, but some texts drop the 2. A note would help readers who compare sources.
