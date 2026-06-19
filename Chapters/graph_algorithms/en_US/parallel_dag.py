from graphlib import TopologicalSorter
tasks = {
    "Compile": set(),
    "Build Frontend": {"Compile"},
    "Build Backend": {"Compile"},
    "Test": {"Build Frontend", "Build Backend"},
    "Deploy": {"Test"},
}
from graphlib import TopologicalSorter

ts = TopologicalSorter(tasks)
ts.prepare()

while ts.is_active():
    ready = ts.get_ready()
    print(ready)

    for task in ready:
        ts.done(task)

