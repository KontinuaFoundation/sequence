import json
import os
import shutil

import util

vol_count = 36

if not os.path.exists("user.cfg"):
    shutil.copyfile("Support/default.cfg", "user.cfg")

with open("user.cfg", "r") as f:
    config = json.load(f)

book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]
books_metadata = []
duplicates = []
sequence_prereq_error = []
all_topics = {}

# Pass 1: build complete global topic index (no prereq checks yet).
for book in book_nums:
    print(f"Parsing resources for {book}...")
    book_metadatas, topics = util.gather_data("../Chapters", book, config)
    books_metadata.append(book_metadatas)

    for topic_key, tdict in topics.items():
        topic_key = topic_key.strip()
        if topic_key in all_topics:
            duplicates.append(
                (topic_key, all_topics[topic_key]["chap_id"], tdict["chap_id"])
            )
        else:
            all_topics[topic_key] = tdict

# Sequential position of each chapter.
chap_pos = {}
chap_info = {}
pos = 0
for book_idx, book_metadatas in enumerate(books_metadata, start=1):
    for chapter in book_metadatas:
        chap_id = chapter.get("id")
        if chap_id and chap_id not in chap_pos:
            chap_pos[chap_id] = pos
            chap_info[chap_id] = (chapter.get("title"), book_idx)
            pos += 1

# Pass 2: check prerequisites.
for book_idx, book_metadatas in enumerate(books_metadata, start=1):
    for chapter in book_metadatas:
        chap_title = chapter.get("title", "Unknown Title")
        chap_id = chapter.get("id")
        requires = [r.strip() for r in chapter.get("requires", []) if isinstance(r, str)]
        for req in requires:
            if req not in all_topics:
                sequence_prereq_error.append({
                    "chap_title": chap_title,
                    "book": book_idx,
                    "req": req,
                    "kind": "missing",
                    "later_chap_id": None,
                })
                continue

            req_chap_id = all_topics[req].get("chap_id")
            if chap_id in chap_pos and req_chap_id in chap_pos:
                if chap_pos[req_chap_id] > chap_pos[chap_id]:
                    sequence_prereq_error.append({
                        "chap_title": chap_title,
                        "book": book_idx,
                        "req": req,
                        "kind": "out_of_order",
                        "later_chap_id": req_chap_id,
                    })

print("--------------")
for e in sequence_prereq_error:
    if e["kind"] == "missing":
        print(f"\U0001F6D1 Book {e['book']:<2} | {e['chap_title']:<40} | requires {e['req']:<20} | MISSING")
    else:
        later_title, later_book = chap_info.get(e["later_chap_id"], (e["later_chap_id"], "?"))
        print(
            f"\U0001F6D1 Book {e['book']:<2} | {e['chap_title']:<40} | requires {e['req']:<20} "
            f"| found later: Book {later_book:<2} | {later_title:<30}"
        )
print("--------------")
for d in duplicates:
    print(f"\u26A0\uFE0F  DUPLICATE TOPIC {d[0]}: origin: {d[1]} \u2192 duplicated in: {d[2]}")
print("--------------")

out_dict = {
    topic: {"desc": t["desc"], "chap_id": t["chap_id"]}
    for topic, t in all_topics.items()
}

with open("../Chapters/topic_index.json", "w") as f:
    json.dump(out_dict, f, indent=2)

print("made Chapters/topic_index.json")
