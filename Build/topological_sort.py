import argparse
import json
import shutil
from collections import defaultdict
from graphlib import CycleError, TopologicalSorter
from pathlib import Path

from graphviz import Digraph

import util


def parse_args():
    parser = argparse.ArgumentParser(
        description="Build graph.json and optional graph image from workbook metadata."
    )
    parser.add_argument(
        "--image",
        action="store_true",
        help="Also render the dependency graph as graph.png",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    vol_count = 36
    cfg_path = Path("user.cfg")

    if not cfg_path.exists():
        shutil.copyfile(Path("Support") / "default.cfg", cfg_path)

    with cfg_path.open("r") as f:
        config = json.load(f)

    book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]
    books_metadata = []
    owners = {}
    graph = defaultdict(set)
    chapter_to_book = {}

    for book in book_nums:
        print(f"Parsing resources for {book}...")
        book_metadatas, _ = util.gather_data("../Chapters", book, config)

        for chapter in book_metadatas:
            chap_id = chapter.get("id")
            chapter_to_book[chap_id] = book

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
    output = {}

    for topic, prereqs in book_00_graph.items():
        output[topic] = {
            "workbook": str(chapter_to_book.get(topic)).zfill(2),
            "prereqs": list(prereqs),
        }

    path = Path("Workbooks-en_US-Letter") / "graph.json"
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w") as f:
        json.dump(output, f, indent=2)

    print(f"Saved {path}")

    try:
        order = list(TopologicalSorter(graph).static_order())
    except CycleError as e:
        raise RuntimeError(f"cycle detected in dependency graph: {e}") from None

    recommended_path = Path("../Chapters") / "recommended_book_00.txt"
    with recommended_path.open("w") as f:
        for chapter in order:
            f.write(chapter + "\n")

    print(f"Saved {recommended_path}")

    if args.image:
        dot = Digraph()
        dot.attr(rankdir="LR")

        for node, deps in book_00_graph.items():
            dot.node(node)
            for dep in deps:
                dot.edge(dep, node)

        dot.render("graph", format="png", view=True)
        print("Saved graph.png")


if __name__ == "__main__":
    main()