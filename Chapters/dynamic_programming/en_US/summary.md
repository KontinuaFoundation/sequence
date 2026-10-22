# Dynamic Programming: Summary

## What the chapter covers
Introduces dynamic programming through the longest common subsequence:
- a hook about autocorrect, git diff, and DNA;
- Fibonacci recalled from the Recursion chapter: memoization (top-down) versus a bottom-up table, and the two conditions (optimal substructure, overlapping subproblems);
- LCS defined (subsequence vs. order), and why brute force needs 2^n tries;
- the recursive idea from the last letters, with lcs_recursive.py showing 212,591 calls for two 11-letter words;
- the LCS recurrence in a box, a hand-filled SHOE/HOSE table, and the walk back to recover HOE (compared with Dijkstra's prev links);
- lcs.py (bottom-up table, walk-back, a __name__ guard) and its O(nm) cost;
- diff.py, a line-based diff built on the same table, in Git's +/- format;
- a five-step recipe, links to Bellman-Ford and Viterbi, and where the name came from.

## Key ideas
- Dynamic programming = solve each overlapping subproblem once and store it (top-down memoization or a bottom-up table).
- LCS recurrence: match → diagonal + 1; otherwise the max of the cell above and the cell to the left.
- Walking back through the table recovers the actual subsequence; the same walk produces a diff.
- Exponential brute force (2^n) becomes polynomial (n·m cells).

## Changes in this pass
- New chapter, placed at the end of volume 22 after shortest_path and priority_queues (it builds on recursion's memoization and calls Bellman-Ford dynamic programming). To keep volumes balanced, stacks_queues moved from the start of volume 22 to the end of volume 21, after the C chapters; both volumes now have 7 chapters.
- Added pointers in recursion (after memoized Fibonacci) and intro_markov (where dynamic programming was mentioned without explanation).
- Three scripts (lcs_recursive.py, lcs.py, diff.py) were run, and their outputs pasted in. All tables and answers were verified in Python (the SHOE/HOSE and CRATE/TRACE tables; RAE as the unique LCS of length 3; SBOARD; 89 ways to climb stairs; fewest coins for 30 cents = 3 vs. greedy 6; spell-check counts 1 and 2; 302 digits in 2^1000).
- 6 exercises with answers (table by hand, climbing stairs, making change where greedy fails, spell check via LCS, table size vs. brute force, substring vs. subsequence).
- The Version Control chapter does not teach git diff, so this chapter introduces it rather than implying students have seen it.
