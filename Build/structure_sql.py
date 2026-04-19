import json
import os
import shutil

import util

vol_count = 36

if not os.path.exists("user.cfg"):
    shutil.copyfile("Support/default.cfg", "user.cfg")

with open("user.cfg", "r") as f:
    config = json.load(f)

filename = "sql.txt"
lang_list = [["en", "US"]]

with open(filename, "w") as fout:
    for x in range(1, vol_count + 1):
        book = str(x).zfill(2)
        print(f"Gathering titles for book {book}...")
        print(f"INSERT INTO mentapp_volume (volume_id) VALUES ({x});", file=fout)
        ids, _ = util.dir_list_for_book("../Chapters", book, config["Languages"])
        order_float = 10.0
        for chap_id in ids:
            print(
                f"INSERT INTO mentapp_chapter (chapter_id, ordering, volume_id) "
                f"VALUES ('{chap_id}', {order_float:.1f}, {x});",
                file=fout,
            )
            order_float += 10.0
            for lang in lang_list:
                iso_code = f"{lang[0]}_{lang[1]}"
                loc_path = f"../Chapters/{chap_id}/{iso_code}"
                if os.path.exists(loc_path):
                    title = util.title_for_dir(loc_path).replace("'", "''")
                    print(
                        f"INSERT INTO mentapp_chapter_loc (lang_code, dialect_code, title, chapter_id) "
                        f"VALUES ('{lang[0]}', '{lang[1]}', '{title}', '{chap_id}');",
                        file=fout,
                    )

print(f"Complete: {filename}")
