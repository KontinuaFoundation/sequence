import json
import os
import shutil

import util

vol_count = 36

if not os.path.exists("user.cfg"):
    shutil.copyfile("Support/default.cfg", "user.cfg")

with open("user.cfg", "r") as f:
    config = json.load(f)

main_locale = config["Languages"][0]
resources_dir = f"Resources-{main_locale}"
os.makedirs(resources_dir, exist_ok=True)

filename = f"{resources_dir}/chaplist.txt"
book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]

with open(filename, "w") as fout:
    for book in book_nums:
        print(f"Gathering titles for book {book}...")
        print(book, file=fout)
        _, dirs = util.dir_list_for_book("../Chapters", book, config["Languages"])
        for d in dirs:
            print(f"\t{util.title_for_dir(d)}", file=fout)

print(f"Complete: {filename}")
