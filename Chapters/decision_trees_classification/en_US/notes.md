# Decision Trees for Classification — Notes

## Summary
Explains how a classification tree asks questions about features, defines Gini impurity G = 1 − Σpᵢ², and shows how a split is chosen by the weighted impurity of its children. The worked split takes a node with G = 0.48 to 0.40 (4 A and 1 B left, 2 A and 3 B right). The chapter also covers overfitting, with depth limits and minimum leaf sizes chosen on a validation set. It has two exercises (G = 0.375 for 3 A and 1 B, and an improvement check with G = 0.25 after the split).

## Changes in this pass
- Added a high school link: the game twenty questions, where a good question splits the possibilities evenly.

## Checked and correct
- Worked example: G = 0.48 before the split; children 0.32 and 0.48; weighted 0.40.
- Exercise dt1: G = 1 − (0.75² + 0.25²) = 0.375.
- Exercise dt2: 0.5(0.2) + 0.5(0.3) = 0.25, which improves on 0.48.

## Open items
- The chapter does not show how the tree picks a threshold for numeric features, which is a common question. A sentence that the tree tries midpoints between sorted values would answer it.
- Entropy and information gain are not mentioned. Readers who see them elsewhere may be confused; a short note would help.
