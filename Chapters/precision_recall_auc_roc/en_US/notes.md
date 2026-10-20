# Evaluating Binary Classifiers Beyond Accuracy — Notes

## Summary
Covers threshold-based measures, the precision–recall tradeoff and curve, the ROC curve (true positive rate against false positive rate) and AUC. It defines AUC as the probability that a random positive scores above a random negative (ties count as half), works an example with AUC = 5/6, and gives guidance on which measure to use. It has two exercises (AUC = 3/4 and a rare-fraud accuracy trap).

## Changes in this pass
- Added a high school link: a fire alarm, where a low threshold rings at every candle and a high threshold misses small fires.

## Checked and correct
- Worked AUC: pairs 3 + 2 = 5 of 6, so AUC = 5/6 ≈ 0.833.
- Exercise prc1: 3 of 4 pairs, AUC = 0.75.
- Exercise prc2: 99% accuracy with no frauds found, so recall is 0.

## Open items
- The ROC section gives the pairwise AUC definition but no ROC table for the worked example. A table of TPR and FPR at each threshold would show how the curve is built.
- The sentence on precision–recall curves and rare classes is correct, but the reason could be stated more directly: the many true negatives keep the false positive rate small.
