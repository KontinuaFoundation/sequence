import enum
import os
import sys
import json
import util
import shutil

# How many volumes are there?
vol_count = 36

# Does the user not have a config file?
if not os.path.exists("user.cfg"):
    # Give them the default
    shutil.copyfile("Support/default.cfg", "user.cfg")

# Read in the config 
with open("user.cfg", "r") as config_fd:
    config = json.load(config_fd)

# Gather all metadatas    
book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]
books_metadata = []
duplicates = [] # ideally empty
sequencePrereqError = [] # ideally empty

# every topic (only)
all_topics = {}
# loop through every individual book
# pass 1: build the complete global topic index (no prereq checks yet)

for book in book_nums:
    print(f"Parsing resources for {book}...")
    # this is the magic line to check prerequisites

    # topics = all "covers" from that book
    (book_metadatas, topics) = util.gather_data("../Chapters", book, config)
    books_metadata.append(book_metadatas)

    # duplicate checker (WORKING)
    for topic_key, tdict in topics.items():
        # when indexing topics
        topic_key = topic_key.strip()
        if topic_key in all_topics:                         # seen before
            first_chap = all_topics[topic_key]['chap_id']   # original
            this_chap  = tdict['chap_id']                   # duplicate
            duplicates.append((topic_key, first_chap, this_chap))
        else:                                               # first sighting
            all_topics[topic_key] = tdict                   # store as-is

# converts chapters into a sequential order
chap_pos = {}     # chap_id -> position int
chap_info = {}    # chap_id -> (title, book_num)
pos = 0

for book_idx, book_metadatas in enumerate(books_metadata, start=1):
    for chapter in book_metadatas:
        chap_id = chapter.get("id")
        chap_title = chapter.get("title")
        if chap_id and chap_id not in chap_pos:
            chap_pos[chap_id] = pos
            chap_info[chap_id] = (chap_title, book_idx)
            pos += 1
            
# pass 2: check prerequisites out-of-order using full index
for book_idx, book_metadatas in enumerate(books_metadata, start=1):
    for chapter in book_metadatas:
        #for each chapter, get its title, id, and prereqs
        chap_title = chapter.get('title', 'Unknown Title')
        chap_id = chapter.get('id')
        requires = [r.strip() for r in chapter.get("requires", []) if isinstance(r, str)]
        for req in requires:
            # missing prereq topic entirely
            if req not in all_topics:
                sequencePrereqError.append({
                    "chap_title": chap_title,
                    "book": book_idx,
                    "req": req,
                    "kind": "missing",
                    "later_chap_id": None,
                })
                continue

            # prereq exists but appears later than this chapter
            req_chap_id = all_topics[req].get('chap_id')
            if chap_id in chap_pos and req_chap_id in chap_pos:
                if chap_pos[req_chap_id] > chap_pos[chap_id]:
                    sequencePrereqError.append({
                        "chap_title": chap_title,
                        "book": book_idx,
                        "req": req,
                        "kind": "out_of_order",
                        "later_chap_id": req_chap_id,
                    })

        
print("--------------")
for e in sequencePrereqError:
    chap_title = e["chap_title"]
    req = e["req"]
    kind = e["kind"]
    current_book = e["book"]
    later_chap_id = e["later_chap_id"]

    if kind == "missing":
        print(f"🛑 Book {current_book:<2} | {chap_title:<40} | requires {req:<20} | MISSING")
    else:
        later_title, later_book = chap_info.get(later_chap_id, (later_chap_id, "?"))
        print(f"🛑 Book {current_book:<2} | {chap_title:<40} | requires {req:<20} | found later: Book {later_book:<2} | {later_title:<30}")
print("--------------")
for d in duplicates:
    print(f"⚠️ DUPLICATE TOPIC {d[0]}: origin: {d[1]} → duplicated in: {d[2]}")

print("--------------")

out_dict = {}
for topic, tdict in all_topics.items():
    out_dict[topic] = {"desc":tdict["desc"], "chap_id":tdict["chap_id"]}

with open("../Chapters/topic_index.json", "w") as f:
    json.dump(out_dict,f, indent=2)

print("made Chapters/topic_index.json")