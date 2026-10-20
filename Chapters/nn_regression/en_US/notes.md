# Neural Networks for Regression — Notes

## Summary
Connects linear regression to neural networks: neurons compute a weighted sum plus a bias and apply an activation (ReLU, sigmoid, tanh), the output layer for regression uses the identity activation, and training follows feedforward, loss, backpropagation, and update. A worked example with ŷ = 2x + 1 on three points gives MSE = 1/3. It has two exercises (a squared error of 1 at (2, 4), and why the output uses the identity activation).

## Changes in this pass
- Added a high school link: a curve on a graph that a straight line cannot follow, but several bent pieces can.

## Checked and correct
- Worked example: predictions 3, 5, 7 for x = 1, 2, 3; errors 0, 0, 1; MSE = 1/3.
- Exercise nnr1: ŷ = 5 at x = 2, so the squared error is 1.
- Exercise nnr2: a sigmoid output lies between 0 and 1, so the identity is used for unbounded targets.

## Open items
- The chapter does not show a hidden layer computation. A two-neuron hidden layer with numbers would show where the nonlinearity enters.
