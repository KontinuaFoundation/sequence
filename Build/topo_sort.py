from graphlib import TopologicalSorter, CycleError
from graphviz import Digraph

import enum
import os
import sys
import json
import util
import shutil
from collections import defaultdict

# This code is copied from make_topic_index.py 
# this loads the graph with chapters as nodes and prerequisites as directed edges

# How many volumes are there?
vol_count = 36

# Does the user not have a config file?
if not os.path.exists("user.cfg"):
    # Give them the default
    shutil.copyfile("Support/default.cfg", "user.cfg")

# Read in the config 
with open("user.cfg", "r") as config_fd:
    config = json.load(config_fd)

# Gather all metadatas    
book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]
books_metadata = []

owners = {}
graph = defaultdict(set) # chapter -> set of prerequisite chapters (edges point from prereq to chapter)
for book in book_nums:
    print(f"Parsing resources for {book}...")
    # this is the magic line to check prerequisites

    # topics = all "covers" from that book
    (book_metadatas, topics) = util.gather_data("../Chapters", book, config)
    books_metadata.append(book_metadatas)

# build owners only, such that topics -> chapters
for book_metadatas in books_metadata:
    for chapter in book_metadatas:
        chap_id = chapter.get("id")
        chap_covers = chapter.get("covers", [])
        for cover in chap_covers:
            topic_id = cover.get("id")
            owners.setdefault(topic_id, chap_id)
            


for book_metadatas in books_metadata:
    for chapter in book_metadatas:
        # nodes
        chap_id = chapter.get("id")
        # edges
        chap_prereqs = chapter.get("requires", [])

        for topic_id in chap_prereqs:
            # check whether a chapter (an owner) teaches that topic and avoid adding a self-dependency if the chapter itself covers the topic (shouldn't exist anyways)
            if topic_id in owners and owners[topic_id] != chap_id:
                graph[chap_id].add(owners[topic_id]) # add the prerequisite chapter as a dependency of the current chapter

        # ensure every chapter is in the graph, even if it has no prereqs
        # if chap_id not in graph:
        #     graph[chap_id] = set()
        # Equivalent code:
        graph.setdefault(chap_id, set()) 

book_00_graph = graph.copy()
           
# print(json.dumps(graph, indent=2, default=list))
      
# attempt topological sort
# graph: every chapter must appear as a key

try:
    ts = TopologicalSorter(graph)
    order = list(ts.static_order())   # linear order of chapters
except CycleError as e:
    raise RuntimeError(f"cycle detected in dependency graph: {e}") from None




# max_len = max(len(existing_order), len(order))

# for i in range(max_len):
#     left = existing_order[i] if i < len(existing_order) else ""
#     if left.startswith("#"):
#         continue
#     right = order[i] if i < len(order) else ""
#     print(f"{i:>3} | {left:<30} | {right}")

# Write the recommended order to a new txt file
with open("../Chapters/recommended_book_00.txt", "w") as f:
    for chapter in order:
        f.write(chapter + "\n")




# generate a visual of our graph!
dot = Digraph()
dot.attr(rankdir="LR")
for node, deps in book_00_graph.items():
    dot.node(node)
    for dep in deps:
        dot.edge(dep, node)
dot.render("graph", format="png", view=True)
