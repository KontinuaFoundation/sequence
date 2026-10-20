# The k-Nearest Neighbor Classifier — Notes

## Summary
Explains k-NN as instance-based learning: compute distances to every training point, take the k nearest, and predict the majority class. It covers the Euclidean distance, a worked example with six labeled points (k = 1 gives B, k = 3 gives A), choosing k on a validation set, feature scaling, and the cost of prediction. It has three exercises that reuse the worked example and a scaling question.

## Changes in this pass
- Added a high school link: asking your nearest friends what movie to watch.

## Checked and correct
- Distances from (1, 2.5): to (2, 3) is √1.25 ≈ 1.118; to (1, 1) is 1.5; to (2, 1) is √3.25 ≈ 1.803. The next points, (4, 1) at about 3.35 and (5, 4) at about 4.27, are farther.
- k = 1 gives B. k = 3 gives B, A, A, so A.
- The scaling exercise: income differences dwarf height differences.

## Open items
- The exercises reuse the worked example. A new point with a different k would test the idea more fully.
- The chapter does not show a standardized version of the six points, so the scaling section is not illustrated numerically.
