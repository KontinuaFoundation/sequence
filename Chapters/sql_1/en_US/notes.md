# Data Tables in SQL — Notes

## Summary
Introduces SQL with sqlite: opening bikes.db, .schema, SELECT with WHERE, DISTINCT, UPDATE, INSERT, and DELETE, then a short Python script (report.py) that runs a query through the sqlite3 module.

## Strengths
- Each sqlite example is shown with the real output, and the outputs match bikes.db (1,000 rows, the schema, the first five rows, the GT-after-2009 query).
- Clear progression from reading to changing data.

## Weaknesses
- **Exercise mismatch:** the question asks for Trek bikes over $300, but the answer and report.py use `purchase_price > 330`. At $300 the query returns 22 rows, not 5.
- **Python bug:** report.py calls `datetime.date.today()` but never imports `datetime`, so it raises NameError. The `today` variable is unused.
- **Wrong highlighting:** the Python script is set in `minted{sql}`, not `minted{python}`.
- **Leftover placeholder:** the text reads "The asterisk (FIXME) used above".
- **Wording:** "from the dataframe" should be "from the table".
- **Raw URL:** the Obsidian Dataview footnote gives a bare URL.
- **Stray comment:** a `%` note at the end proposes a sql_2 chapter, which now exists.

## Index entries added
relational database, WHERE, DISTINCT, UPDATE, INSERT, DELETE, sqlite3 (Python library).

## Editor to-do
- Change the answer and report.py threshold to match the question ($300), or change the question.
- Import datetime (or remove the unused line) and set the code to Python.
- Replace the FIXME and remove the stray comment.
