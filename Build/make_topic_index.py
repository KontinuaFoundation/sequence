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
all_topics = {}
for book in book_nums:
    print(f"Parsing resources for {book}...")
    # this is the magic line to check prerequisites
    (book_metadatas, topics) = util.gather_data("../Chapters", book, config)
    books_metadata.append(book_metadatas)
    all_topics.update(topics)
print(books_metadata[0][4]['requires'])
# chapter prereqs are at books_metadata[0][CHAPTERNUM]['requires']
#TODO 
# - check all "covers" ids are unique
# - check all "requires" ids are previously defined in covers sections

out_dict = {}
for topic, tdict in all_topics.items():
    out_dict[topic] = {"desc":tdict["desc"], "chap_id":tdict["chap_id"]}

with open("../Chapters/topic_index.json", "w") as f:
    json.dump(out_dict,f, indent=2)

print("made Chapters/topic_index.json")