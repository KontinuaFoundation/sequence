# Sorting and Big-O Notation — Notes

## Summary
New chapter. Introduces selection sort, insertion sort, and merge sort with tested Python code. Introduces Big-O notation with a formal definition, a table of common classes, and a step-count table that compares n, n log n, and n² for several sizes. Ends with four exercises and answers.

## Strengths
- All three sorting listings were run against Python's `sorted()` on 200 random lists.
- The comparison counts for selection and insertion sort on reverse-sorted input were checked by counting in code.

## Weaknesses
- The chapter has no images or figures; a diagram of merge sort's halving would help.
- Merge sort's comparison count is given only as O(n log n), not as an exact count.

## Index entries added
sorting, Big-O notation (with a definition subentry), selection sort, insertion sort, merge sort, sorting comparison.

## Editor to-do
- Add a short prerequisite line at the start (lists, loops, and functions from the Python chapters).
- Consider a figure showing how merge sort splits and merges a small list.
