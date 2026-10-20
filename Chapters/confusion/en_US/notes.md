# Evaluating Classification Systems — Notes

## Summary
Defines the confusion matrix (TP, FP, FN, TN), accuracy, precision, recall, specificity, and F₁. A worked example uses 200 screening results (TP = 40, FP = 10, FN = 20, TN = 130) to give accuracy 0.85, precision 0.80, recall 0.667, specificity 0.929, and F₁ ≈ 0.727. It ends with a discussion of which metric to choose and three exercises.

## Changes in this pass
- Added a high school link: a school metal detector, where a false positive stops a student by mistake and a false negative misses a weapon, so recall matters more.

## Checked and correct
- Every worked metric: accuracy 170/200 = 0.85; precision 40/50 = 0.80; recall 40/60 ≈ 0.667; specificity 130/140 ≈ 0.929; F₁ ≈ 0.727.
- Exercise conf1: accuracy 0.80 and precision ≈ 0.857.
- Exercise conf3: a classifier that always predicts negative has 95% accuracy and 0 recall when 5% are positive.

## Open items
- Specificity appears in the metric list but has no exercise. Add a short question on specificity.
- The chapter has one worked example. The standard format asks for a couple of worked problems. A second worked example (for example, a spam filter with precision as the focus) would help.
