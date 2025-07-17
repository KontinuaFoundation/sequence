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
for book in book_nums:
    print(f"Parsing resources for {book}...")
    # this is the magic line to check prerequisites

    # topics = all "covers" from that book
    (book_metadatas, topics) = util.gather_data("../Chapters", book, config)
    books_metadata.append(book_metadatas)

    # duplicate checker (WORKING)
    # previously was: # all_topics.update(topics)

    for topic_key, tdict in topics.items():
        if topic_key in all_topics:                         # seen before
            first_chap = all_topics[topic_key]['chap_id']   # original
            this_chap  = tdict['chap_id']                   # duplicate
            duplicates.append((topic_key, first_chap, this_chap))
            # print(f"⚠️ DUPLICATE topicID '{topic_key}': {first_chap} → {this_chap}") PRINTING after
        else:                                               # first sighting
            all_topics[topic_key] = tdict                   # store as-is

    # check prerequisites before adding new topics (logical order)
    for chapter in book_metadatas:
        chap_title = chapter.get('title', 'Unknown Title')
        # chap_id = chapter.get('id', 'Unknown ID')
        requires = chapter.get('requires', [])
        for req in requires:
            if req not in all_topics:
                sequencePrereqError.append((chap_title, req));
                # print(f"🛑🛑🛑 {chap_title} requires {req} but not covered previously")

print("--------------")
for item in sequencePrereqError:
    print(f"🛑🛑🛑 {item[0]} requires {item[1]} but not covered previously")
   
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