# Neural Networks for Classification — Notes

## Summary
Changes the output layer and loss for classification: a sigmoid output for two classes, softmax for more than two, and cross-entropy loss L = −[y ln p + (1 − y) ln(1 − p)]. The worked example uses z = 1, p = σ(1) ≈ 0.731, and a loss of about 0.313 when the label is 1. It has two exercises (σ(0) = 0.5, and a loss of about 2.303 for p = 0.1 with label 1).

## Changes in this pass
- Added a high school link: a weather forecast that gives a 10% chance of rain on a rainy day, where cross-entropy punishes the forecast heavily.

## Checked and correct
- σ(1) = 1/(1 + e⁻¹) ≈ 0.731, and −ln(0.731) ≈ 0.313.
- Exercise nnc1: σ(0) = 0.5.
- Exercise nnc2: −ln(0.1) ≈ 2.303.

## Open items
- The softmax formula is named but not written. A one-line formula, softmax(z)_i = e^{z_i} / Σ_j e^{z_j}, would make the multi-class case concrete.
- The chapter does not show a multi-class cross-entropy example. A three-class worked example would match the multi-class claim in the output section.
