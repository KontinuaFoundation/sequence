import datetime
import enum
import json
import os
import shutil
import sys

from jinja2 import Environment, FileSystemLoader

import util


def usage():
    print("Usage: python3 make_web.py <iso_code>")
    sys.exit(1)


# How many volumes are there?
vol_count = 36

# Check command line
if len(sys.argv) < 2:
    usage()

chap_file = "student.tex"
workdir = "Intermediate"
if not os.path.exists(workdir):
    os.mkdir(workdir)
os.chdir(workdir)

# For page size and latex command
with open("../user.cfg", "r") as config_fd:
    config = json.load(config_fd)

# Change local to just the language being generated
config["Languages"] = [sys.argv[1]]

resources_dir = f"../Resources-{config['Languages'][0]}"

# Make the directory if necessary
if not os.path.exists(resources_dir):
    print(f"Making {resources_dir}")
    # os.makedirs(resources_dir)

# Gather all metadatas
book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]
mod_dir = "../../Chapters"

failures = []
for book_str in book_nums:
    (result_ids, result_paths) = util.dir_list_for_book(
        mod_dir, book_str, config["Languages"]
    )
    # print(f"{book_str}:{result_ids}, {result_paths}")
    chap_count = len(result_ids)
    for chap in range(chap_count):
        # outfile = os.path.join(resources_dir, f"{result_ids[chap]}.pdf")
        outfile = resources_dir + f"/{result_ids[chap]}.pdf"
        print(f"{book_str}:{chap}: Making {outfile}")
        success = util.build_chapter(
            chap_file, result_paths[chap], config, outfile, draft=True, date_check=True
        )
        if not success:
            failures.append(outfile)
if len(failures) > 0:
    print(f"Unable to build {failures}")
