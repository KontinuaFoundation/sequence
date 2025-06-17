import os
import datetime
import json
import util
import shutil
import sys
import urllib.request
import time
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    print("Usage: python3 <days>")
    print(" Any link that has been confirmed in the last <days> is assumed unchanged")
    print(" If <days> is zero, always refetch")
    exit(1)

day_count = int(sys.argv[1])

# How many volumes are there?
vol_count = 36

# Does the user not have a config file?
if not os.path.exists("user.cfg"):
    # Give them the default
    shutil.copyfile("Support/default.cfg", "user.cfg")

# Read in the config
with open("user.cfg", "r") as config_fd:
    config = json.load(config_fd)

# Linkfile
dirpath = f"Resources-{config['Languages'][0]}"
if not os.path.exists(dirpath):
    os.makedirs(dirpath)

linkpath = f"{dirpath}/Links.json"

# Read the last lookup
if os.path.exists(linkpath):
    with open(linkpath,"r") as f:
        old_links = json.load(f)
else:
    old_links = {}

now = datetime.datetime.now()
now_str = now.isoformat(timespec='minutes')

if day_count > 0:
    fetch_if_after = now - datetime.timedelta(days=day_count)
    print("Refetching anything not fetched since {fetch_if_after.date}")
else:
    fetch_if_after = None
    print("Refetching everything")

# Gather all metadatas
print("Reading metadata for all books")
book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]
all_chaps = []
for book in book_nums:
    (book_chaps, _) = util.gather_data("../Chapters", book, config)
    all_chaps.extend(book_chaps)

# maps url -> {title:"", confirmed:datetime}
new_links = {}

# Which ones were unfetchable?
broken_links = []
count = 0
for chap_meta in all_chaps:
    # What URLs are videos and references for this chapter?
    urls = util.urls_in_chapter_meta(chap_meta)
    if len(urls) > 0:
        print(f"Fetching for {chap_meta['id']} ({chap_meta['title']})...")
        for url in urls:
            # Maybe I don't need to fetch this?
            if fetch_if_after is not None and url in old_links:
                link_data = old_links[url]
                if 'date' in link_data:
                    old_fetch = datetime.datetime.fromisoformat(link_data['date'])
                    # Can I skip the fetch?
                    if old_fetch > fetch_if_after:
                        # Copy the old data into the new dict
                        new_links[url] = link_data
                        print(f"\tSkipping {url}: Cached {link_data['date']}")
                        # Go on to the next URL
                        continue

            print(f"\tFetching {url}")
            req = urllib.request.Request(url)
            try:
                response = urllib.request.urlopen(req)
            except urllib.error.HTTPError as e:
                print(f"Error for {chap_meta['id']} {url}: The server couldn\'t fulfill the request.")
                print('Error code: ', e.code)
                broken_links.append({'chap_id':chap_meta['id'], 'url':url, 'error': e.code})
                continue
            except urllib.error.URLError as e:
                print(f"Error for {url}: Failed to reach server.")
                print('Reason: ', e.reason)
                continue

            data = None
            while data is None:
                try:
                    data = response.read()
                except Exception as e:
                    print("read failed. Waiting 10 seconds and trying again")
                    time.sleep(10)
                    response = urllib.request.urlopen(req)

            soup = BeautifulSoup(data, "html.parser")
            head = soup.head
            title = head.title.string
            print(f"\t\tTitle:\"{title}\"")
            new_links[url] = {'title':title, 'date':now_str}

with open(linkpath,"w") as f:
    json.dump(new_links, f, indent=2)

print(f"Done. Saved in {linkpath}")

if len(broken_links) > 0:
    print("Broken links:")
    for link in broken_links:
        print(f"{link['chap_id']}, Error {link['error']}, {link['url']} ")
