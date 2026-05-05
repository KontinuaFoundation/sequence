import json
import os
import sys
from pathlib import Path
import util


def usage(exit_code=0):
    print(
        "Usage:\n"
        "  python3 make_chapter_pdfs.py <iso_code> [--force]\n\n"
        "Options:\n"
        "  <iso_code>   required, the language to build in. en_US for English\n"
        "  --force      Force rebuild of chapter PDFs (disables date checks)\n"
    )
    sys.exit(exit_code)


args = sys.argv[1:]

if "-h" in args or "--help" in args:
    usage(0)

force = "--force" in args
if force:
    args.remove("--force")

if len(args) != 1:
    usage(1)

iso_code = args[0]
date_check = None if force else True
VOL_COUNT = 36

chap_file = "student.tex"
BUILD_DIR = Path.cwd() 
ROOT_DIR = BUILD_DIR.parent
CHAPTERS_DIR = ROOT_DIR / "Chapters"
USR_CFG = BUILD_DIR / "user.cfg"
INTERMEDIATE_DIR = BUILD_DIR / "Intermediate"  
 
INTERMEDIATE_DIR.mkdir(parents=True, exist_ok=True)
os.chdir(INTERMEDIATE_DIR)

with USR_CFG.open("r") as f:
    config = json.load(f)

config["Languages"] = [iso_code]

RESOURCES_DIR = BUILD_DIR / f"Resources-{iso_code}"
os.makedirs(RESOURCES_DIR, exist_ok=True)

book_nums = [str(x).zfill(2) for x in range(1, VOL_COUNT + 1)]

failures = []
for book_str in book_nums:
    result_ids, result_paths = util.dir_list_for_book(
        CHAPTERS_DIR, book_str, config["Languages"]
    )
    for chap, chap_id in enumerate(result_ids):
        outfile = f"{RESOURCES_DIR}/{chap_id}.pdf"
        print(f"{book_str}:{chap}: Making {outfile}")
        success = util.build_chapter(
            chap_file,
            result_paths[chap],
            config,
            outfile,
            draft=True,
            date_check=date_check,
        )
        if not success:
            failures.append(outfile)

if failures:
    print(f"Unable to build {failures}")
    sys.exit(1)
