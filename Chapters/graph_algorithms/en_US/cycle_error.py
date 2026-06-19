from graphlib import TopologicalSorter
graph = {
  "C": {"A", "B"},
  "A": {"Z"},
  "B": {"Z"},
  "Z": {"C"}
}
list(TopologicalSorter(graph).static_order())
