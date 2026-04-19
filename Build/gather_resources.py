import datetime
import json
import os
import re
import shutil
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

import util

vol_count = 36

environment = Environment(loader=FileSystemLoader("Support"))
template = environment.get_template("resource_template.html")

if not os.path.exists("user.cfg"):
    shutil.copyfile("Support/default.cfg", "user.cfg")

with open("user.cfg", "r") as f:
    config = json.load(f)

main_locale = config["Languages"][0]
resources_dir = f"Resources-{main_locale}"

linkpath = f"{resources_dir}/Links.json"
if not os.path.exists(linkpath):
    print(f"Run url_check first to create {linkpath}")
    sys.exit(1)

with open(linkpath, "r") as f:
    links = json.load(f)

os.makedirs(resources_dir, exist_ok=True)
shutil.copyfile("Support/kontinua.css", f"{resources_dir}/kontinua.css")

book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]
books_metadata = []
all_topics = {}
for book in book_nums:
    print(f"Indexing book {book}...")
    book_metadatas, topics = util.gather_data("../Chapters", book, config)
    books_metadata.append(book_metadatas)
    all_topics.update(topics)

today_str = datetime.datetime.now().isoformat(timespec="minutes")
books = []
chapters = {}

for i in range(vol_count):
    book_str = str(i + 1).zfill(2)
    metadatas = books_metadata[i]
    content = template.render(
        topics=all_topics,
        chapters=metadatas,
        book_str=book_str,
        today_str=today_str,
        links=links,
        pdf_href=f"workbook-{book_str}.pdf",
    )
    path = f"{resources_dir}/Workbook-{book_str}.html"
    with open(path, mode="w", encoding="utf-8") as out:
        out.write(content)
    print(f"Wrote {path}")
    books.append(book_str)
    chapters[book_str] = metadatas

index_template = environment.get_template("index_template.html")
indexname = f"{resources_dir}/index.html"
with open(indexname, mode="w", encoding="utf-8") as out:
    out.write(index_template.render(books=books, chapters=chapters))
print(f"Wrote {indexname}")

OUTPUT_FILE = Path(resources_dir) / "workbooks.json"
_WB_RE = re.compile(r"workbook-(\d+)\.json$", re.IGNORECASE)


def _workbook_num(path: Path) -> int:
    m = _WB_RE.search(path.name)
    if not m:
        raise ValueError(f"Unexpected filename: {path.name}")
    return int(m.group(1))


def convert_workbook(path: Path) -> dict:
    num = _workbook_num(path)
    with path.open("r", encoding="utf-8") as f:
        chapters_raw = json.load(f)

    return {
        "title": f"Workbook {num:02d}",
        "href": f"Workbook-{num:02d}.html",
        "pdf": f"Workbook-{num:02d}.pdf",
        "chapters": [
            {"id": c["id"], "title": c["title"], "chap_num": c["chap_num"]}
            for c in chapters_raw
        ],
    }


files = sorted(Path(resources_dir).glob("workbook-*.json"), key=_workbook_num)
workbooks = [convert_workbook(p) for p in files]

with OUTPUT_FILE.open("w", encoding="utf-8") as f:
    json.dump(workbooks, f, indent=2, ensure_ascii=False)

print(f"Wrote {OUTPUT_FILE} with {len(workbooks)} workbooks.")
