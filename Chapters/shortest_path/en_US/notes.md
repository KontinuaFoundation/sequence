# Finding Shortest Paths — Notes

## Summary
Shows why BFS fails on weighted graphs, then develops Dijkstra's algorithm with the Long Beach shipping example (Bakersfield improves from $22 to $21 via San Diego), tracks dist and prev in dictionaries, implements cost_from_node and shortest_path in Python, and introduces Bellman-Ford for negative edges.

## Strengths
- The shipping example is worked step by step, and the cost values match the graph (Los Angeles $12, San Diego $14, Bakersfield $21, Sacramento $32).
- The "why BFS fails" example (A→C costs $6, A→B→C costs $3) is clear.
- The shortest_path function correctly walks prev back to the origin.
- Bellman-Ford's |V| − 1 passes and negative-cycle check are stated correctly.

## Weaknesses
- **Syntax error:** `print(f"*** Cheapest path from Long Beach to NYC: {path_to_nyc ***}")` has the brace in the wrong place.
- **Mismatched LaTeX environment:** the text output block opens with minted and closes with `\end{text}`.
- **Commented-out material:** a large commented section (priority queue speedup) remains in the source.
- **Unclear reference:** "This action... is done in lines 16-21" refers to code line numbers that do not match the listing.
- **Missing exercise answers:** the Bellman-Ford section has no worked example or exercise.

## Index entries added
shortest path, weighted graph, BFS limitations, Dijkstra's algorithm, predecessor tree, negative cycle. The chapter already had Dijkstra, Edsger.

## Editor to-do
- Fix the f-string and the \end{text} mismatch.
- Add a Bellman-Ford worked example.
