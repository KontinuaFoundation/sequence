# Data Tables in SQL — Notes

## Summary
Introduces relational databases and SQL with the sqlite command-line tool and the bikes.db file. It covers .schema, SELECT (all columns, chosen columns, WHERE with AND and OR, DISTINCT), UPDATE, INSERT, and DELETE. It ends with a short Python program that runs a query with the sqlite3 library. It has an exercise with an answer.

## Changes in this pass
- Made the price threshold consistent at $330 in the exercise, its answer, and the Python example.
- Removed the leftover "(FIXME)" from the asterisk sentence.
- Changed "dataframe" to "table," since this is a database, not pandas.
- Removed an unused datetime line from the Python example (datetime was used without an import).
- Changed the Python listing's language tag from SQL to Python.

## Open items
- The chapter needs a second exercise, for example an UPDATE or a query with AND and OR.
- The Python sample output was generated from the original data. Re-run it against the current bikes.db before publishing.
- A comment at the end says a second SQL chapter is planned. `sql_2` is that chapter, so the comment can be removed.
