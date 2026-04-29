import argparse
import json
import os
import shutil
import sys
from pathlib import Path

import util

VOL_COUNT = 36


def parse_args():
    parser = argparse.ArgumentParser(
        description="Build enriched workbooks.json from chapter metadata and Links.json."
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
        help="Optional file containing chapter IDs (one per line); ignored (always full build).",
    )
    return parser.parse_args()


def main():
    parse_args()

    if not os.path.exists("user.cfg"):
        shutil.copyfile("Support/default.cfg", "user.cfg")

    with open("user.cfg", "r", encoding="utf-8") as f:
        config = json.load(f)

    main_locale = config["Languages"][0]
    resources_dir = f"Resources-{main_locale}"
    os.makedirs(resources_dir, exist_ok=True)

    linkpath = f"{resources_dir}/Links.json"
    if not os.path.exists(linkpath):
        print(f"Run gather_resources.py first to create {linkpath}")
        sys.exit(1)

    with open(linkpath, "r", encoding="utf-8") as f:
        links = json.load(f)

    def resolve(url):
        return {"url": url, "title": links.get(url, {}).get("title", url)}

    mod_dir = "../Chapters"
    book_nums = [str(x).zfill(2) for x in range(1, VOL_COUNT + 1)]

    workbooks = []
    for book in book_nums:
        print(f"Building workbook {book}...")
        chapters_raw, _ = util.gather_data(mod_dir, book, config)

        chapters = []
        for c in chapters_raw:
            covers = [
                {
                    "id": t["id"],
                    "desc": t.get("desc", ""),
                    "videos": [resolve(u) for u in t.get("videos", [])],
                    "references": [resolve(u) for u in t.get("references", [])],
                }
                for t in c.get("covers", [])
            ]
            chapters.append(
                {
                    "id": c["id"],
                    "title": c["title"],
                    "chap_num": c["chap_num"],
                    "files": c.get("files", []),
                    "requires": c.get("requires", []),
                    "covers": covers,
                }
            )

        workbooks.append(
            {
                "num": book,
                "title": f"Workbook {book}",
                "pdf": f"workbook-{book}.pdf",
                "chapters": chapters,
            }
        )

    output_file = Path(resources_dir) / "workbooks.json"
    with output_file.open("w", encoding="utf-8") as f:
        json.dump(workbooks, f, indent=2, ensure_ascii=False)

    print(f"Wrote {output_file} with {len(workbooks)} workbooks.")


if __name__ == "__main__":
    main()
