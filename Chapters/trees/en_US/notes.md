# Trees — Notes

## Summary
Defines trees (root, edges, siblings, leaves, depth, height, subtrees), explains why a tree has n − 1 edges, introduces binary search trees with a seven-word example, shows insertion, and applies trees to file-system hierarchies with a path exercise.

## Changes in this pass
- Fixed the definition of a tree. A tree is a connected graph with no cycles. The old text said graphs are "converted" into trees by adding constraints.
- Corrected the claim that computers date from the 1980s.
- Removed the stray "Test again test again test again" and fixed "A node is naturally fits."
- Finished the insertion example: orange goes to the left of peach. Added a note that a new node is always a leaf, and an exercise (insert kiwi, which becomes the right child of banana).
- Removed the FIXME notes for the tree proof, the insertion explanation, and the exercise that is now written.

## Strengths
- The depth, height, and leaf definitions match Figure 2 (height 3, leaves are the grandchildren level).
- The seven-word binary search tree satisfies the search-tree ordering at every node.
- The file-system path exercise is correct: ./Documents/Projects/project2/data.csv has depth 4.

## Open items
- Two sections are still placeholders: "Red-Black Trees and AVL Trees" and "B-Trees, Tries, and Suffix Trees." Write them or remove them.
- The chapter does not cover deletion or search in a binary search tree in detail.
- The "Advanced Python Syntax" reference (in the next chapter) should be checked against the book list.
