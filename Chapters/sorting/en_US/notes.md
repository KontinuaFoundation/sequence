# Sorting and Big-O Notation — Notes

## Summary
Introduces three sorting algorithms with tested Python code (selection sort, insertion sort, merge sort), then Big-O notation with its definition, a table of common classes, and a step-count table. It compares the sorts by their number of comparisons and ends with four exercises and answers.

## Changes in this pass
- Added a worked example that traces selection sort on [5, 2, 9, 1] (three passes, with the list after each pass). The trace was run and checked.
- Removed contractions (none were left).

## Checked
- All three sorting listings agree with Python's sorted() on 200 random lists.
- The comparison counts for selection and insertion sort on reverse-sorted input match n(n-1)/2.

## Open items
- The chapter has no figures. A diagram of merge sort's splits and merges would help.
- Add a prerequisite line that names the lists and loops chapters.
