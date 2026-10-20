# Other Graph Algorithms and Proofs — Notes

## Summary
Covers adjacency lists and matrices (undirected and directed), Prim's algorithm for minimum spanning trees, A* search with heuristics, injection/surjection/bijection and graph isomorphism, the clique reduction, a short TSP section, topological sort with graphlib, and proofs (bipartite graphs, cycle detection, leaf removal, strongly connected graphs).

## Changes in this pass
- Corrected the loop convention in the adjacency matrix. The figure shows one loop on D, so the diagonal entry is 1 (2 in some texts).
- Removed the duplicate F–G edge in the weighted-graph answer.
- Wrote the Prim's algorithm section (it was a one-line stub with a FIXME). Renamed the heading to match the content. Added a worked example (total weight 17) and an exercise starting from G (also 17).
- Wrote a short TSP section with the nearest-neighbour heuristic, in place of a FIXME.
- Fixed the FindOdd condition. It used pre- and post-order numbers; the parity test needs DFS depths (level).
- Strengthened the bipartite proof: an odd closed walk contains an odd cycle.
- Rewrote the leaf-removal proof. The old version was circular. The new version uses a DFS tree and the fact that removing a leaf keeps a tree connected.
- Corrected the definition of strong connectivity (a single vertex reaching all others is not enough). Fixed the description of strongly connected components.
- Removed a duplicated block of the parallel-tasks Python code, and a visible FIXME Diagram.
- Fixed definitions: injection (inputs, not integers), surjection/bijection wording, the isomorphism invariant list, "much harder," the A* text (g is updated, not g(n), and "to to").
- Removed the duplicated sentence in the A* section.

## Strengths
- The adjacency list and matrix for the four-node graph are correct, and the directed matrix is correct.
- The weighted-graph exercise answer matches the matrix.
- The injection/surjection/bijection exercise answers are correct.
- The clique-to-subgraph-isomorphism reduction is stated correctly.
- The topological-sort examples and the graphlib formats are correct.

## Open items
- The CycleError message shown in the text is copied from one run. Check the exact message before publishing.
- The section on proofs has a "% FIXME Example environment" comment (in the source only).
