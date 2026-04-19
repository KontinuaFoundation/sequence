import json
import os
import shutil
from collections import defaultdict
from graphlib import CycleError, TopologicalSorter

from graphviz import Digraph

import util

vol_count = 36

if not os.path.exists("user.cfg"):
    shutil.copyfile("Support/default.cfg", "user.cfg")

with open("user.cfg", "r") as f:
    config = json.load(f)

book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]
books_metadata = []
owners = {}
graph = defaultdict(set)

for book in book_nums:
    print(f"Parsing resources for {book}...")
    book_metadatas, _ = util.gather_data("../Chapters", book, config)
    books_metadata.append(book_metadatas)

# topics -> owning chapter id
for book_metadatas in books_metadata:
    for chapter in book_metadatas:
        chap_id = chapter.get("id")
        for cover in chapter.get("covers", []):
            owners.setdefault(cover.get("id"), chap_id)

for book_metadatas in books_metadata:
    for chapter in book_metadatas:
        chap_id = chapter.get("id")
        for topic_id in chapter.get("requires", []):
            if topic_id in owners and owners[topic_id] != chap_id:
                graph[chap_id].add(owners[topic_id])
        graph.setdefault(chap_id, set())

book_00_graph = dict(graph)

try:
    order = list(TopologicalSorter(graph).static_order())
except CycleError as e:
    raise RuntimeError(f"cycle detected in dependency graph: {e}") from None

with open("../Chapters/recommended_book_00.txt", "w") as f:
    for chapter in order:
        f.write(chapter + "\n")

dot = Digraph()
dot.attr(rankdir="LR")
for node, deps in book_00_graph.items():
    dot.node(node)
    for dep in deps:
        dot.edge(dep, node)
dot.render("graph", format="png", view=True)
