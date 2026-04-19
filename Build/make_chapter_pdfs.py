import json
import os
import sys

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
vol_count = 36

chap_file = "student.tex"
workdir = "Intermediate"
os.makedirs(workdir, exist_ok=True)
os.chdir(workdir)

with open("../user.cfg", "r") as f:
    config = json.load(f)

config["Languages"] = [iso_code]

resources_dir = f"../Resources-{iso_code}"
os.makedirs(resources_dir, exist_ok=True)

book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]
mod_dir = "../../Chapters"

failures = []
for book_str in book_nums:
    result_ids, result_paths = util.dir_list_for_book(
        mod_dir, book_str, config["Languages"]
    )
    for chap, chap_id in enumerate(result_ids):
        outfile = f"{resources_dir}/{chap_id}.pdf"
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
