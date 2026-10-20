# Finding Shortest Paths — Notes

## Summary
Explains why BFS fails on weighted graphs, walks through Dijkstra's algorithm on a five-city shipping example with predecessor pointers, implements cost_from_node and shortest_path in Python, and ends with Bellman-Ford for negative edge weights.

## Changes in this pass
- Fixed the f-string in the final print statement (`{path_to_nyc ***}` was a syntax error).
- Changed the mismatched `\end{text}` to `\end{minted}`.
- Replaced a reference to "lines 16-21" with a description of the loop's last part.
- Added an unworked exercise: Dijkstra's algorithm by hand on a five-node graph. Answer: costs 0, 2, 3, 5, and the path A → B → C → D.

## Strengths
- The Long Beach example is correct: Los Angeles 12, San Diego 14, Bakersfield 21 (via San Diego), Sacramento 32, and the predecessor pointers match.
- The BFS counterexample (weights 1, 2, and 6) is correct: A → B → C costs 3, and A → C costs 6.
- The Bellman-Ford steps are correct.

## Open items
- The printed outputs in the Python section were written by hand. Run the code before publishing them.
