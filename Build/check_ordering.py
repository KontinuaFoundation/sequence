#!/usr/bin/env python3
"""Check that every chapter's prerequisites come before it in the reading order.

Reads Chapters/book_00.txt (the order of every chapter in the series), then
reads each chapter's digital_resources.json, from the first chapter to the last.
Each file lists the topic ids the chapter "covers" and the ids it "requires".
At the end, the script reports:

  1. Chapters that have no digital_resources.json file.
  2. Chapters whose digital_resources.json file does not parse.
  3. Chapters that require an id that no chapter in book_00.txt covers.
  4. Chapters that require an id that is first covered by a later chapter.

A requirement that the chapter covers itself is not reported.

Usage:
    python3 check_ordering.py [--locale en_US]

The exit status is 0 if no problems were found and 1 otherwise.
"""

import argparse
import json
import sys
from pathlib import Path

BUILD_DIR = Path(__file__).resolve().parent
CHAPTERS_DIR = BUILD_DIR.parent / "Chapters"


def read_book(path):
    """Return the chapter ids listed in a book_NN.txt file, skipping comments."""
    ids = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            ids.append(line)
    return ids


def volume_of_each_chapter():
    """Map each chapter id to its volume number, using book_01.txt, book_02.txt, ..."""
    volumes = {}
    for path in sorted(CHAPTERS_DIR.glob("book_[0-9][0-9].txt")):
        number = int(path.stem.split("_")[1])
        if number == 0:
            continue
        for chapter in read_book(path):
            volumes[chapter] = number
    return volumes


def as_list(value):
    """The JSON files sometimes hold a single string where a list is expected."""
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    return list(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--locale", default="en_US", help="chapter locale folder (default: en_US)")
    args = parser.parse_args()

    order = read_book(CHAPTERS_DIR / "book_00.txt")
    volumes = volume_of_each_chapter()

    def where(chapter):
        number = volumes.get(chapter)
        return f"{chapter} (Vol {number})" if number else f"{chapter} (not in any volume)"

    missing_file = []      # chapters with no digital_resources.json
    unparsable = []        # (chapter, error message)
    requires = {}          # chapter -> list of required ids
    first_covered = {}     # id -> (position in book_00.txt, chapter) of the first chapter that covers it
    covers = {}            # chapter -> set of ids it covers

    # Pass 1: read every file in reading order, recording where each id is first covered.
    for position, chapter in enumerate(order):
        path = CHAPTERS_DIR / chapter / args.locale / "digital_resources.json"
        if not path.exists():
            missing_file.append(chapter)
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                raise ValueError("the top level is not a JSON object")
            chapter_covers = set()
            for entry in as_list(data.get("covers")):
                topic = entry.get("id") if isinstance(entry, dict) else entry
                if not isinstance(topic, str) or not topic:
                    raise ValueError(f"a 'covers' entry has no id: {entry!r}")
                chapter_covers.add(topic)
                first_covered.setdefault(topic, (position, chapter))
            covers[chapter] = chapter_covers
            requires[chapter] = [r for r in as_list(data.get("requires")) if isinstance(r, str)]
        except (json.JSONDecodeError, ValueError, AttributeError, UnicodeDecodeError) as error:
            unparsable.append((chapter, str(error)))

    # Pass 2: check each chapter's requirements against what came before it.
    nonexistent = []       # (chapter, id)
    out_of_order = []      # (chapter, id, chapter that first covers it)
    for position, chapter in enumerate(order):
        for topic in requires.get(chapter, []):
            if topic in covers.get(chapter, set()):
                continue
            if topic not in first_covered:
                nonexistent.append((chapter, topic))
            else:
                covered_at, covered_by = first_covered[topic]
                if covered_at > position:
                    out_of_order.append((chapter, topic, covered_by))

    # Report
    def heading(title, count):
        print(f"\n{title}: {count}")
        print("-" * (len(title) + len(str(count)) + 2))

    print(f"Checked {len(order)} chapters listed in {CHAPTERS_DIR / 'book_00.txt'}")

    heading("Chapters with no digital_resources.json", len(missing_file))
    for chapter in missing_file:
        print(f"  {where(chapter)}")

    heading("Chapters whose digital_resources.json does not parse", len(unparsable))
    for chapter, error in unparsable:
        print(f"  {where(chapter)}: {error}")

    heading("Requirements that no chapter covers", len(nonexistent))
    chapter_names = set(order)
    for chapter, topic in nonexistent:
        hint = ""
        if topic in chapter_names:
            hint = " (this is a chapter name, not an id that a chapter covers)"
        print(f"  {where(chapter)} requires '{topic}'{hint}")

    heading("Requirements that are first covered by a later chapter", len(out_of_order))
    for chapter, topic, covered_by in out_of_order:
        print(f"  {where(chapter)} requires '{topic}', first covered by {where(covered_by)}")

    problems = len(missing_file) + len(unparsable) + len(nonexistent) + len(out_of_order)
    print(f"\n{problems} problem(s) found.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
