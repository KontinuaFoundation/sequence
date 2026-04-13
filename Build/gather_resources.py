import os
import datetime
from pathlib import Path
import re
import json
import util
import shutil
from jinja2 import Environment, FileSystemLoader

# How many volumes are there?
vol_count = 36

# Get the template for the per-book file
environment = Environment(loader=FileSystemLoader("Support"))
template = environment.get_template("resource_template.html")

# Does the user not have a config file?
if not os.path.exists("user.cfg"):
    # Give them the default
    shutil.copyfile("Support/default.cfg", "user.cfg")

# Read in the config
with open("user.cfg", "r") as config_fd:
    config = json.load(config_fd)

# Name the directory after the user's favorite locale
main_locale = config["Languages"][0]
resources_dir = f"Resources-{main_locale}"

# Linkfile
linkpath = f"Resources-{main_locale}/Links.json"
if os.path.exists(linkpath):
    with open(linkpath,"r") as f:
        links = json.load(f)
else:
    print(f"Run url_check first to create {linkpath}")
    exit(1)

# Make the directory if necessary
if not os.path.exists(resources_dir):
    os.makedirs(resources_dir)

# Copy in the stylesheet
shutil.copyfile("Support/kontinua.css", f"{resources_dir}/kontinua.css")

# Gather all metadatas
book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]
books_metadata = []
all_topics = {}
for book in book_nums:
    print(f"Indexing book {book}...")
    (book_metadatas, topics) = util.gather_data("../Chapters", book, config)
    books_metadata.append(book_metadatas)
    all_topics.update(topics)

# Walk the workbooks making a HTML for each
book_indices = list(range(vol_count))
# For gathering data for the index.html
books = []
chapters = {}
today_str = datetime.datetime.now().isoformat(timespec='minutes')

for i in book_indices:
    book_str = str(i + 1).zfill(2)
    metadatas = books_metadata[i]
    pdf_href = f"workbook-{book_str}.pdf"
    content = template.render(
        topics=all_topics, 
        chapters=metadatas, 
        book_str=book_str, 
        today_str=today_str, 
        links=links,
        pdf_href=pdf_href
        )
    filename = f"Workbook-{book_str}.html"
    path = f"{resources_dir}/{filename}"
    # print(f"Writing {path}")
    with open(path, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"Wrote {path}")
        books.append(book_str)
        chapters[book_str] = metadatas

# Use the stuff gathered to make an index
index_template = environment.get_template("index_template.html")
content = index_template.render( books=books, chapters=chapters)
indexname = f"{resources_dir}/index.html"
with open(indexname, mode="w", encoding="utf-8") as message:
    message.write(content)
    print(f"Wrote {indexname}")

# rewrite index.html content into a react valid resource as json

OUTPUT_FILE = Path(resources_dir) / "workbooks.json"


def workbook_sort_key(path: Path):
    m = re.search(r"workbook-(\d+)\.json$", path.name, re.IGNORECASE)
    return int(m.group(1)) if m else 9999


def workbook_title_from_filename(path: Path) -> str:
    m = re.search(r"workbook-(\d+)\.json$", path.name, re.IGNORECASE)
    if not m:
        raise ValueError(f"Unexpected filename: {path.name}")
    return f"Workbook {int(m.group(1)):02d}"


def workbook_href_from_filename(path: Path) -> str:
    m = re.search(r"workbook-(\d+)\.json$", path.name, re.IGNORECASE)
    if not m:
        raise ValueError(f"Unexpected filename: {path.name}")
    return f"Workbook-{int(m.group(1)):02d}.html"

def workbook_pdf_from_filename(path: Path) -> str:
    m = re.search(r"workbook-(\d+)\.json$", path.name, re.IGNORECASE)
    if not m:
        raise ValueError(f"Unexpected filename: {path.name}")
    return f"Workbook-{int(m.group(1)):02d}.pdf"

def convert_workbook(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        chapters_raw = json.load(f)

    chapters = []
    for item in chapters_raw:
        chapters.append(
            {
                "id": item["id"],
                "title": item["title"],
                "chap_num": item["chap_num"],
            }
        )

    return {
        "title": workbook_title_from_filename(path),
        "href": workbook_href_from_filename(path),
        "pdf": workbook_pdf_from_filename(path),
        "chapters": chapters,
    }


files = sorted(Path(resources_dir).glob("workbook-*.json"), key=workbook_sort_key)

workbooks = [convert_workbook(path) for path in files]

with OUTPUT_FILE.open("w", encoding="utf-8") as f:
    json.dump(workbooks, f, indent=2, ensure_ascii=False)

print(f"Wrote {OUTPUT_FILE} with {len(workbooks)} workbooks.")

