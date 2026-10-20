# Introduction to Python — Notes

## Summary
A first Python course: installing Python and VS Code, print() with separators and end, datatypes (str, int, float, bool, list, dict), variables and type(), arithmetic and augmented assignment, input() with casting, conditionals, for and while loops, match-case, and indexing, slicing, and methods for strings and lists. Most sections end with a short exercise and an answer.

## Strengths
- Writing-first approach ("type out the lines yourself") suits beginners.
- Strong, step-by-step coverage of input/casting and common errors (TypeError, ValueError).
- Exercises such as the backpack list trace build the habit of tracing code.

## Weaknesses
- **Wrong output:** `print(d // b)` with d = −100, b = 3 gives −34, but the block shows 34.
- **Wrong example:** the nested-list code prints `numbers[...]` (the earlier list) instead of `nested_numbers`; the outputs 0, 3, 5 do not follow.
- **Wrong claim:** "set" is listed under sequence types whose values are "accessed by positions," but sets are unordered.
- **Wrong text:** "seq[:] returns a copy of the given string" (it is a list).
- **Subsection mismatch:** "Slicing Strings" covers lists too; slicing syntax uses "stop," not "end."
- **Overstatement:** an infinite loop "risks hardware component issues."
- **Typos:** "No we are not talking," "an indexe," "strung-nested lists," "Let's talk more about the print() statement."
- **Scope:** "Introduction" has no section on functions yet, and the closing section promises a later workbook.

## Index entries added
variable, sequential execution, infinite loop, slicing, mutable, immutable, ValueError, indentation. (Existing: 31 entries kept.)

## Editor to-do
- Fix the −34 output and the nested-list example.
- Correct the set and seq[:] wording.
