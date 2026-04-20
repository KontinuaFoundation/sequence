import argparse
import datetime
import json
import os
import shutil
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

import util

VOL_COUNT = 36


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Render workbook HTML/index resources using Links.json. "
            "Can be limited to books affected by changed chapters."
        )
    )
    parser.add_argument(
        "days",
        nargs="?",
        default=None,
        help="Legacy positional argument kept for compatibility; ignored.",
    )
    parser.add_argument(
        "--chapters-file",
        type=str,
        default="",
        help="Optional file containing chapter IDs (one per line).",
    )
    return parser.parse_args()


def load_changed_chapters(path):
    chapter_ids = []
    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            chapter = raw.strip()
            if chapter and not chapter.startswith("#"):
                chapter_ids.append(chapter)
    return set(chapter_ids)


def affected_books_for_chapters(mod_dir, chapter_ids, langlist):
    if not chapter_ids:
        return set()

    affected = set()
    for n in range(1, VOL_COUNT + 1):
        book = str(n).zfill(2)
        ids, _ = util.dir_list_for_book(mod_dir, book, langlist)
        if any(ch in chapter_ids for ch in ids):
            affected.add(book)
    return affected


def main():
    args = parse_args()
    chapters_file = args.chapters_file.strip()
    incremental = bool(chapters_file)

    environment = Environment(loader=FileSystemLoader("Support"))
    template = environment.get_template("resource_template.html")

    if not os.path.exists("user.cfg"):
        shutil.copyfile("Support/default.cfg", "user.cfg")

    with open("user.cfg", "r", encoding="utf-8") as f:
        config = json.load(f)

    main_locale = config["Languages"][0]
    resources_dir = f"Resources-{main_locale}"
    os.makedirs(resources_dir, exist_ok=True)
    shutil.copyfile("Support/kontinua.css", f"{resources_dir}/kontinua.css")

    linkpath = f"{resources_dir}/Links.json"
    if not os.path.exists(linkpath):
        print(f"Run gather_resources.py first to create {linkpath}")
        sys.exit(1)

    with open(linkpath, "r", encoding="utf-8") as f:
        links = json.load(f)

    mod_dir = "../Chapters"
    book_nums = [str(x).zfill(2) for x in range(1, VOL_COUNT + 1)]
    if incremental:
        changed_chapters = load_changed_chapters(chapters_file)
        affected_books = affected_books_for_chapters(mod_dir, changed_chapters, config["Languages"])
        print(f"Incremental mode for {len(changed_chapters)} chapter(s). Affected books: {sorted(affected_books)}")
    else:
        affected_books = set(book_nums)

    books_metadata = {}
    all_topics = {}
    for book in book_nums:
        print(f"Indexing book {book}...")
        book_metadatas, topics = util.gather_data(mod_dir, book, config)
        books_metadata[book] = book_metadatas
        all_topics.update(topics)

    today_str = datetime.datetime.now().isoformat(timespec="minutes")
    for book in sorted(affected_books):
        metadatas = books_metadata[book]
        content = template.render(
            topics=all_topics,
            chapters=metadatas,
            book_str=book,
            today_str=today_str,
            links=links,
            pdf_href=f"workbook-{book}.pdf",
        )
        path = f"{resources_dir}/Workbook-{book}.html"
        with open(path, mode="w", encoding="utf-8") as out:
            out.write(content)
        print(f"Wrote {path}")

    # Index always reflects all books/chapters.
    index_template = environment.get_template("index_template.html")
    indexname = f"{resources_dir}/index.html"
    with open(indexname, mode="w", encoding="utf-8") as out:
        out.write(index_template.render(books=book_nums, chapters=books_metadata))
    print(f"Wrote {indexname}")

    output_file = Path(resources_dir) / "workbooks.json"
    workbooks = []
    for book in book_nums:
        chapters_raw = books_metadata[book]
        workbooks.append(
            {
                "title": f"Workbook {book}",
                "href": f"Workbook-{book}.html",
                "pdf": f"Workbook-{book}.pdf",
                "chapters": [
                    {"id": c["id"], "title": c["title"], "chap_num": c["chap_num"]}
                    for c in chapters_raw
                ],
            }
        )

    with output_file.open("w", encoding="utf-8") as f:
        json.dump(workbooks, f, indent=2, ensure_ascii=False)

    print(f"Wrote {output_file} with {len(workbooks)} workbooks.")


if __name__ == "__main__":
    main()
