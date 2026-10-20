# Priority Queues — Notes

## Summary
Builds a priority queue for Dijkstra's algorithm in two stages: a naive sorted-list version, then a binary-search insertion version. Shows how graph.py changes to use it, how a TypeError arises from tied priorities, and how defining Node.__lt__ fixes it. Ends with a binary search explanation using a phone-book analogy.

## Strengths
- The phone-book analogy makes binary search intuitive.
- The naive-to-efficient progression shows why the change matters.
- The tie-breaking bug is shown with a reproducible example and a fix.

## Weaknesses
- **Module name mismatch:** the import is `kpqueue` but the code calls `pqueue.PriorityQueue()`.
- **Wrong reference:** the TypeError explanation names `loc_for_pair`, which does not exist until the later section. In the naive version, the error comes from `list.sort()`.
- **Typo:** "This should be have exactly the same result."
- **Duplicate code:** the PriorityQueue class is repeated in full in the binary-search section.
- **FIXME:** the binary search section has a time-complexity FIXME that is unaddressed.
- **Inefficiency left unmeasured:** pop() uses list.pop(0), which is O(n). The chapter does not mention it.

## Index entries added
priority queue (and naive implementation, graph search, binary search insertion), Dijkstra's algorithm, binary search algorithm, TypeError.

## Editor to-do
- Fix the import name and the loc_for_pair reference.
- Address the time-complexity FIXME and the pop(0) cost.
