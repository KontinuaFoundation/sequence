# Bagging and Random Forests — Notes

## Summary
Explains bagging (bootstrap aggregating: train on n points drawn with replacement and combine by averaging or voting), why a bootstrap sample contains about 63.2% of distinct points (1 − 1/e), random forests (a random subset of k features at each split, k = √p for classification and p/3 for regression), and out-of-bag error. It includes a worked example for n = 10 (0.349 missed, about 65% distinct) and two exercises (a 5-point left-out probability of 0.328, and k = 4 for 16 features).

## Changes in this pass
- Added a worked example: for n = 10, (0.9)¹⁰ ≈ 0.349 chance of being missed, so about 65% of distinct points appear.
- Added a high school link: asking several friends for restaurant suggestions and taking the most popular choice.

## Checked and correct
- The limit (1 − 1/n)ⁿ → 1/e ≈ 0.368, so about 63.2% of distinct points appear.
- Exercise bag1: (0.8)⁵ ≈ 0.328.
- Exercise bag2: k = √16 = 4.

## Open items
- The out-of-bag claim that the error is "an honest estimate of test error" holds under the usual assumptions. A sentence on those assumptions would help.
