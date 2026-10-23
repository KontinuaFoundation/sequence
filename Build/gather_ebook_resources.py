import json
import os
import re
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
    print(f"Run gather_resources.py to create {link_file}")
    sys.exit(1)

with open(link_file, "r") as f:
    links = json.load(f)

book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]

# In the .toc file, the answers are a lettered appendix chapter and the index is
# an unnumbered "starchapter" entry:
#   \contentsline {chapter}{\numberline {A}Answers to Exercises}{57}{appendix.A}%
#   \contentsline {starchapter}{\numberline {}Index}{63}{section*.13}%
answers_pattern = re.compile(r"\{chapter\}\{\\numberline \{[A-Z]\}Answers[^}]*\}\{([0-9]+)\}")
index_pattern = re.compile(r"\{starchapter\}\{\\numberline \{\}Index\}\{([0-9]+)\}")


def back_matter(book, chap_count):
    """Table of contents entries for the answers and the index of a volume."""
    with open(f"Intermediate/workbook-{book}.toc") as f:
        toc = f.read()
    entries = []
    for title, pattern in (("Answers", answers_pattern), ("Index", index_pattern)):
        match = pattern.search(toc)
        if match is None:
            print(f"\tNo {title} entry in Intermediate/workbook-{book}.toc")
            continue
        entries.append({
            "id": f"{title.lower()}-{book}",
            "title": title,
            "chap_num": chap_count + len(entries) + 1,
            "start_page": int(match.group(1)),
            "covers": [],       # the server and the reader apps require this key
        })
    return entries

for book in book_nums:
    print(f"Indexing book {book}...")
    chapter_datas, topics = util.gather_data("../Chapters", book, config)

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
                    # Leave out links that gather_resources.py could not get a title for
                    title = links.get(url, {}).get("title", "").strip()
                    if not title:
                        print(f"\tSkipping {url} ({t['chap_id']}): no title in {link_file}")
                        continue
                    out_list.append({"link": url, "title": title})
                topic_dict[key] = out_list

        chapter_datas[chap_idx]["covers"].append(topic_dict)

    chapter_datas.extend(back_matter(book, len(chapter_datas)))

    outpath = f"{resources_dir}/workbook-{book}.json"
    with open(outpath, "w") as f:
        json.dump(chapter_datas, f, indent=2)
    print(f"Wrote {outpath}")
