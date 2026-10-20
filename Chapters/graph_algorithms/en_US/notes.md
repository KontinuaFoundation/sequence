# Other Graph Algorithms and Proofs — Notes

## Summary
Covers adjacency matrices, A* search (f = g + h, admissibility), injection/surjection/bijection and isomorphism, a clique reduction, topological sort with graphlib, and proofs on bipartite graphs, cycle detection, leaf removal, and strong connectivity.

## Strengths
- The adjacency matrix examples are correct, including the 4×4 undirected matrix and the weighted exercise (symmetric, and matched by the answer graph).
- The A* description is correct: admissibility is stated, and h = 0 reduces A* to Dijkstra.
- The injection/surjection/bijection answers are all correct.
- The bipartite theorem and its proof are clear, and the cycle-detection and strong-connectivity answers are correct.

## Weaknesses
- **Placeholder section:** "Prim's Algorithm and Kruskal's Algorithm" has one sentence and a FIXME. Traveling Salesperson is also a FIXME.
- **Duplicate edge:** the exercise answer draws the F–G edge twice.
- **Broken code:** the parallel_dag.py listing contains a duplicated block, and the closing brace is joined to the next import (`}from graphlib import ...`).
- **Figure vs text:** the text says "two edges" from D to itself, but the figure draws one loop.
- **Duplicate sentence:** "Each time we visit a node, we have a decision to make" appears twice in the A* section.
- **Questionable proof step:** the leaf-removal proof is unclear and writes G / {l} for G − {l}.
- **Unverified pseudocode:** FindOdd tests pre(x) − post(y); check the convention.

## Index entries added
adjacency matrix, adjacency list, A* search, heuristic, admissible heuristic, graph isomorphism, topological sort, bipartite graph, strongly connected.

## Editor to-do
- Write Prim's and Kruskal's or move them out, and remove the duplicate edge.
- Fix the parallel_dag.py listing and the duplicated sentence.
- Check FindOdd against the DFS convention and fix the proof wording.
