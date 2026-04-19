import json
import os
import shutil
import sys

import util

vol_count = 36

if not os.path.exists("user.cfg"):
    shutil.copyfile("Support/default.cfg", "user.cfg")

with open("user.cfg", "r") as f:
    config = json.load(f)

main_locale = config["Languages"][0]
resources_dir = f"Resources-{main_locale}"

link_file = f"{resources_dir}/Links.json"
if not os.path.exists(link_file):
    print(f"Run url_check.py to create {link_file}")
    sys.exit(1)

with open(link_file, "r") as f:
    links = json.load(f)

book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]
all_topics = {}

for book in book_nums:
    print(f"Indexing book {book}...")
    chapter_datas, topics = util.gather_data("../Chapters", book, config)
    all_topics.update(topics)

    toc_dict = util.chapter_toc(book)

    for i, chapter_meta in enumerate(chapter_datas):
        chapter_page = toc_dict[str(i + 1)]
        chapter_meta["covers"] = []
        chapter_meta["start_page"] = chapter_page
        chapter_meta.pop("files", None)
        chapter_meta.pop("book", None)

    for tid, t in topics.items():
        chap_idx = t["chap_num"] - 1
        topic_dict = {"id": tid, "desc": t["desc"]}

        for key in ("videos", "references"):
            if key in t:
                out_list = []
                for url in t[key]:
                    title = links[url]["title"] if url in links else "???"
                    out_list.append({"link": url, "title": title})
                topic_dict[key] = out_list

        chapter_datas[chap_idx]["covers"].append(topic_dict)

    outpath = f"{resources_dir}/workbook-{book}.json"
    with open(outpath, "w") as f:
        json.dump(chapter_datas, f, indent=2)
    print(f"Wrote {outpath}")

for topic_id in all_topics:
    all_topics[topic_id].pop("videos", None)
    all_topics[topic_id].pop("references", None)

outpath = f"{resources_dir}/topic_index.json"
with open(outpath, "w") as f:
    json.dump(all_topics, f, indent=2)
print(f"Wrote {outpath}")
