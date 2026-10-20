# Data Tables and pandas — Notes

## Summary
Introduces tables (primary keys, data types, nulls, categorical columns) and then pandas: reading bikes.csv, shape, Series statistics, value counts, row access with iloc and loc, cleaning mislabeled and missing status values with boolean masks, and deriving an age column from a date string.

## Strengths
- A hands-on program that builds step by step, with expected output shown after each step.
- Cleaning the status column demonstrates a real data-quality problem (case, a synonym, missing values).
- Shows several equivalent ways to access one value, which helps students read others' code.

## Weaknesses
- **Missing import:** the code uses `datetime.date` in three places, but `import datetime` never appears.
- **Wrong column name:** the text says the new file will have an "age_by_date" column; the code creates "age_in_days."
- **Incomplete sentence:** "Let's ask for one entry from the" ends with no continuation.
- **Typos:** "fined" (find), "Next, the each bike," "''available''" (mismatched quotes), "1 bikes are" (plural).
- **Expected output:** the age values (for example, 13061 days) depend on today's date and will not match when the code is run later.

## Index entries added
Series, DataFrame, primary key, categorical variable, comma-separated values, pandas!index. (Existing: datatypes, null, pandas.)

## Editor to-do
- Add `import datetime` and fix the column name.
- Note that the age output changes with the run date.
