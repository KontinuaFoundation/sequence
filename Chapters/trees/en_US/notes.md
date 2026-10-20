# Trees — Notes

## Summary
Defines trees (nodes, edges, root, siblings, n−1 edges, forests), depth, height, levels, ancestors and descendants, and binary search trees with a seven-word dictionary example. Applies trees to file-system directories and works a path and depth exercise.

## Strengths
- The n−1 edge argument is clear and correct.
- The BST example is correct: seven words, mango as root, height 2.
- The file-system tree maps cleanly to the concept, and the depth exercise (4) is correct.

## Weaknesses
- **Incomplete sections:** the proof, BST insert, search, and delete, plus the red-black, AVL, B-tree, trie, and suffix-tree sections, are FIXME placeholders. The BST insertion text ends mid-sentence ("Because of alphabetical sorting,").
- **Factual error:** "Computers, since their first creation in the 1980s" is wrong. Computers predate the 1980s.
- **Stray text:** "Test again test again test again" appears in the directory section.
- **Typos:** "Let's put this practice," "A node is naturally fits," "in anywhere on your computer's memory."
- **Unclear sentence:** "Moving from one node to the next is the recursive step that minimizes the size."
- **Figure label:** "Depth = 2" is drawn on the brace from root to a leaf, so it reads as the tree's depth. The height label is correct.
- **Wording:** "Graphs can be converted into trees by adding ... constraints" should say restricting or imposing constraints.
- **Cross-reference:** "our binary search implementation from the recursion chapter" is not checked.

## Index entries added
tree, root, depth, height of a tree, subtree, binary search tree, binary tree, directory, file system hierarchy.

## Editor to-do
- Fill the FIXME sections, starting with BST operations.
- Correct the 1980s claim and the stray text.
