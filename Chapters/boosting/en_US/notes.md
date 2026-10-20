# Boosting — Notes

## Summary
Introduces boosting as combining weak learners, then AdaBoost for labels in {−1, +1}: equal starting weights, weighted error εₜ, αₜ = ½ ln((1 − εₜ)/εₜ), and the weight update with normalization. A worked round with four points gives α₁ = ½ ln 3 ≈ 0.549, misclassified weight 0.5, and correct weights 1/6 each. It also covers gradient boosting (each tree fits the negative gradient, which for squared error is the residual) and cautions about overfitting. It has two exercises (α = 1.099 for ε = 0.1, and which points gain weight).

## Changes in this pass
- Added a high school link: after each practice test, spend more time on the problems you missed.

## Checked and correct
- Worked round: α₁ = ½ ln 3 ≈ 0.549. Correct points get (1/4)e^{−0.549} ≈ 0.144 each, and the misclassified point gets (1/4)e^{0.549} ≈ 0.433. The total is 0.866, so after normalizing the misclassified point has weight 0.5 and each correct point has 1/6 ≈ 0.167.
- Exercise bst1: α = ½ ln 9 ≈ 1.099.
- Exercise bst2: misclassified points gain weight because e^{α} > 1.

## Open items
- The gradient boosting paragraph says the gradient for squared error is "just the residual." Strictly, it is the negative of the residual up to a constant factor. The sentence is accurate in meaning but could say "the residual, up to a factor of 2."
- Learning rate and the number of rounds are discussed in one sentence. A sentence on the trade-off would connect this to the validation discussion.
