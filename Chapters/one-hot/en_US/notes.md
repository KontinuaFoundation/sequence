# One-Hot Encoding — Notes

## Summary
Explains categorical variables, one-hot encoding (one binary column per category, exactly one 1 per row), the dummy variable trap and why one column is dropped in linear and logistic regression, and when to use integer codes for ordered categories instead. It has two exercises: encoding sizes (small, medium, large, small) and explaining the dropped column.

## Changes in this pass
- Added a high school link: a survey about favorite subject, where each answer becomes its own yes or no column.

## Checked and correct
- Exercise oh1: (1,0,0), (0,1,0), (0,0,1), (1,0,0).
- Exercise oh2: the columns sum to 1 in every row, so they are linearly dependent with the intercept.

## Open items
- The chapter has no worked example with a data table in a standard format. The color table works as one, but a labeled worked example (for example, with a column dropped and the resulting coefficient interpretation) would match the standard.
