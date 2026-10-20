# Tree Traversal — Notes

## Summary
Covers breadth-first search with a queue (level order, with a trace table and search pseudocode), depth-first search with pre-order, in-order, and post-order orders, an iterative DFS pseudocode, recursive DFS, and pre- and post-order numbering with a worked numbering table.

## Strengths
- The BFS trace table is correct at every step, and the final level-order output is right.
- The pre-, post-, and in-order sequences for the seven-name tree are all correct.
- The pre- and post-order numbering table is correct, and the recursive pre-order answer is correct.

## Weaknesses
- **Wrong pre-order claim:** the iterative DFS pseudocode pushes left and then right. A stack pops right first, so the sequence is not pre-order. The text says it "corresponds to a pre-order traversal." To get pre-order, push right first, then left.
- **Typo:** "do have a preselected node a your start node."
- **Unclear phrase:** "the three orders in which we can traverse/search the deepest tree."
- **Stale comments:** several FIXME notes (exercise on BFS, queues defined later, and stacks/queues as prerequisites that do not exist yet).
- **Heading style:** "\section{BFS}" and "\section{DFS}" have no intro, unlike the other sections.
- **Overreach:** BFS use cases (maze solvers, chess, tic-tac-toe) are listed without explanation.

## Index entries added
tree traversal, breadth-first search, level-order traversal, depth-first search, pre-order traversal, post-order traversal, in-order traversal, recursive traversal, pre-order number.

## Editor to-do
- Fix the iterative DFS push order or the "pre-order" claim.
- Add the BFS exercise and resolve the prerequisite FIXMEs.
