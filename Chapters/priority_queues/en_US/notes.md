# Priority Queues — Notes

## Summary
Builds a priority queue for Dijkstra's algorithm: a naive sorted-list version, changes to the graph search to use it, the fix for ties with __lt__ based on id(), and a faster version using binary search for insertion. Ends with a working binary search explanation.

## Changes in this pass
- Removed the claim that Dijkstra's algorithm was covered in the last chapter. The chapter now introduces it briefly.
- Fixed the import: `import kpqueue` now matches `kpqueue.PriorityQueue()`.
- Corrected the comment on pop(): it returns the (cost, city) pair.
- Named the correct function for the search-loop rewrite (the loop in the shortest-path function, not cost_from_node).
- Fixed "should be have" to "should have".
- Explained why binary search takes about log₂ n steps (addresses the old FIXME on time complexity).
- Added a worked example (binary search for 56 in a sorted list of 10 values) and an unworked exercise (search for 38; answer index 6, checking 23, 72, 56, 38).

## Strengths
- The naive version, the update method, and the binary-search insertion code are correct.
- The phone-book picture of binary search is a good everyday link.
- The TypeError message shown matches Python 3.

## Open items
- The chapter uses cities.py and graph.py from earlier code. Say where those files come from if this chapter is read alone.
