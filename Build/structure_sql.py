import enum
import os
import sys
import json
import util
import shutil

vol_count = 36
# Does the user not have a config file?
if not os.path.exists("user.cfg"):
    # Give them the default
    shutil.copyfile("Support/default.cfg", "user.cfg")

# Read in the config
with open("user.cfg", "r") as config_fd:
    config = json.load(config_fd)

# Open the file
filename = f"sql.txt"
fout = open(filename, "w")

# What languages are we trying to localize for?
lang_list = [["en","US"]]

# Walk the books
for x in range(1, vol_count + 1):
    book = str(x).zfill(2)
    print(f"Gathering titles for book {book}...")
    print(f"INSERT INTO mentapp_volume (volume_id) VALUES ({x});", file=fout)
    (ids, dirs) = util.dir_list_for_book("../Chapters", book, config["Languages"])
    order_float = 10.0
    for id in ids:
        print(f"INSERT INTO mentapp_chapter (chapter_id, ordering, volume_id) VALUES ('{id}', {order_float:.1f}, {x});", file=fout)
        order_float += 10.0
        for lang in lang_list:
            iso_code = f"{lang[0]}_{lang[1]}"
            loc_path = f"../Chapters/{id}/{iso_code}"
            if os.path.exists(loc_path):
                title = util.title_for_dir(loc_path)
                title = title.replace("'","''")
                print(f"INSERT INTO mentapp_chapter_loc (lang_code, dialect_code, title, chapter_id) VALUES ('{lang[0]}', '{lang[1]}', '{title}', '{id}');", file=fout)

fout.close()
print(f"Complete: {filename}")
