# Deep Learning — Notes

## Summary
Introduces deep networks as many layers of weighted sums and nonlinear activations, the chain rule with an example (d/dx sin(x² + 1) = 2x cos(x² + 1), which is about −2.339 at x = 1.3), backpropagation for a single weight (∂L/∂w = 2(ŷ − t)x), and practical points about minibatches and vanishing gradients. It has two exercises (d/dx (3x − 1)⁴ = 12(3x − 1)³, and ∂L/∂w = 6 at w = 2, x = 3, t = 5).

## Changes in this pass
- Added a high school link: recognizing a face, from edges to eyes and noses to the whole face.

## Checked and correct
- d/dx sin(x² + 1) at x = 1.3: 2(1.3) cos(2.69) ≈ −2.339.
- Exercise dl1: 12(3x − 1)³.
- Exercise dl2: ŷ = 6, so ∂L/∂w = 2(6 − 5)(3) = 6.

## Open items
- The chapter covers one weight. A two-layer example with a hidden unit would show how backpropagation reuses the forward values.
- The vanishing-gradient sentence names the cause but not the activation function that helps. A sentence naming ReLU would connect to the nn chapters.
