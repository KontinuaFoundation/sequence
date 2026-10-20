# Tree Traversal — Notes

## Summary
Covers breadth-first search with a queue (with a step trace and pseudocode), depth-first search with a stack, the three DFS orders (pre-, post-, in-order) with results for the same seven-name tree, recursive and iterative versions, and pre-order and post-order numbering with an answer table.

## Changes in this pass
- Fixed the iterative DFS pseudocode. It pushed the left child first, so it popped the right child first and visited nodes in the wrong order. It now pushes the right child first, so the left child is popped first, and the pre-order claim holds. Added a sentence explaining the push order.
- Fixed "requires you do have a preselected node a your start node."
- Changed "traverse/search the deepest tree" to "traverse the whole tree."

## Strengths
- The BFS step trace matches the queue rules.
- All traversal results are correct: pre-order Alan, Brad, Dean, Emily, Connie, Faith, Gordon; post-order Dean, Emily, Brad, Faith, Gordon, Connie, Alan; in-order Dean, Brad, Emily, Alan, Faith, Connie, Gordon.
- The pre- and post-order numbers in the answer table are correct, using one shared counter.

## Open items
- The header comments still list "DFS vs BFS from a graph to a tree" and "Searching in BSTs" as planned topics. The chapter does not yet cover searching in BSTs.
- Stacks and queues are cited as prerequisites. They are covered in an earlier chapter in the book.
