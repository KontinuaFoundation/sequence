# The Training, Validation, and Testing Process — Notes

## Summary
Explains why the data is split into training, validation, and test sets, gives a worked 70/15/15 split of 1000 rows, states the rules that keep the sets separate (no fitting on validation or test, no choosing by test score, no leakage through scaling), and introduces k-fold cross-validation. It has three exercises (row counts for 2400 rows, a scaling leak, and choosing k on the test set).

## Changes in this pass
- Added a high school link: practice tests for the validation set, and one real exam for the test set.

## Checked and correct
- The 70/15/15 split of 1000 rows gives 700, 150, and 150.
- The 2400-row split gives 1680, 360, and 360.
- The scaling-leak and test-set-tuning answers match the rules in the section.

## Open items
- The chapter has no worked example with data. Consider a short example of a k-fold split (for example, 5 folds of 200 rows each from 1000 training rows).
