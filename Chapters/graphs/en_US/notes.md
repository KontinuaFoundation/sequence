# Introduction to Graphs — Notes

## Summary
Defines graphs as nodes and edges: directed and undirected examples, degree, paths and cycles, connectivity and connected components, subgraphs, weighted graphs (a shipping network), adjacency lists, and a word-ladder exercise. It ends by writing Node, WeightedEdge, and Graph classes in Python and printing a small city network.

## Strengths
- Each concept has its own small diagram, with the cycle and disconnected-graph examples checked.
- The weighted shipping map motivates shortest-path problems before algorithms appear.
- The Python classes build up gradually and the printed degrees match the figure.

## Weaknesses
- **Code error:** `other_end` is defined at module level (no indentation), so it is a function, not a method of WeightedEdge.
- **Wrong concept:** "In weighted graphs, the degree of a node is split into the in-degree and out-degree." In- and out-degree apply to directed graphs; the shipping graph is undirected.
- **Unsupported claim:** word-ladder graphs are said to be "usually represented as a tree." They are not trees; they contain cycles (for example, bad–bar–bed).
- **Typo:** "Miama."
- **Unfinished:** the chapter promises the next chapter will make the output "more exciting," with no pointer for the word-graph exercise.

## Index entries added
node, edge, degree, cycle, connected component, subgraph, weighted graph, adjacency list. (Existing: graph!directed, graph!undirected, graph!connected.)

## Editor to-do
- Indent `other_end` inside WeightedEdge.
- Fix the in/out-degree sentence and the tree claim.
