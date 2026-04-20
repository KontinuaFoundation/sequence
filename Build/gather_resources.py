import argparse
import datetime
import json
import os
import shutil
import time
import urllib.error
import urllib.request
from pathlib import Path

from bs4 import BeautifulSoup

import util


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Check links in chapter digital resources and write/update "
            "Resources-<locale>/Links.json."
        )
    )
    parser.add_argument(
        "days",
        nargs="?",
        type=int,
        default=90,
        help=(
            "Only refetch URLs not confirmed in the last N days. "
            "Use 0 to refetch everything."
        ),
    )
    parser.add_argument(
        "--chapters-file",
        type=str,
        default="",
        help="Optional file containing chapter IDs (one per line) for incremental checking.",
    )
    return parser.parse_args()


def load_changed_chapters(path):
    chapter_ids = []
    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            chapter = raw.strip()
            if chapter and not chapter.startswith("#"):
                chapter_ids.append(chapter)
    # Preserve order while de-duplicating.
    return list(dict.fromkeys(chapter_ids))


def chapter_meta_for_id(mod_dir, chapter_id, config):
    chapter_dir = util.dir_for_id(mod_dir, chapter_id, config["Languages"])
    student_tex = f"{chapter_dir}/student.tex"
    if not os.path.exists(student_tex):
        print(f"Skipping {chapter_id}: {student_tex} does not exist")
        return None

    md = util.metadata_for_dir(chapter_dir)
    md["id"] = chapter_id
    md["title"] = util.title_for_dir(chapter_dir)
    return md


def chapter_metas_for_all_books(mod_dir, config, vol_count=36):
    all_chaps = []
    book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]
    for book in book_nums:
        book_chaps, _ = util.gather_data(mod_dir, book, config)
        all_chaps.extend(book_chaps)
    return all_chaps


def fetch_title_for_url(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
    }
    req = urllib.request.Request(url, headers=headers)

    try:
        response = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        if e.code == 429:
            retry_after = e.headers.get("Retry-After")
            wait_time = int(retry_after) if retry_after else 10
            print(f"\n\t429 received for {url}. Sleeping {wait_time}s before retry...")
            time.sleep(wait_time)
            response = urllib.request.urlopen(req)
        else:
            raise

    data = None
    while data is None:
        try:
            data = response.read()
        except Exception:
            print("\n\tread failed. Waiting 10 seconds and trying again")
            time.sleep(10)
            response = urllib.request.urlopen(req)

    if ".pdf" in url:
        return os.path.basename(url)

    soup = BeautifulSoup(data, "html.parser")
    head = soup.head
    if head is None or head.title is None or head.title.string is None:
        return url
    return head.title.string


def main():
    args = parse_args()

    day_count = args.days
    chapters_file = args.chapters_file.strip()
    incremental = bool(chapters_file)

    if not os.path.exists("user.cfg"):
        shutil.copyfile("Support/default.cfg", "user.cfg")

    with open("user.cfg", "r", encoding="utf-8") as config_fd:
        config = json.load(config_fd)

    dirpath = f"Resources-{config['Languages'][0]}"
    os.makedirs(dirpath, exist_ok=True)
    linkpath = f"{dirpath}/Links.json"

    if os.path.exists(linkpath):
        with open(linkpath, "r", encoding="utf-8") as f:
            old_links = json.load(f)
    else:
        old_links = {}

    now = datetime.datetime.now()
    now_str = now.isoformat(timespec="minutes")

    if day_count > 0:
        fetch_if_after = now - datetime.timedelta(days=day_count)
        print(f"Refetching anything not fetched since {fetch_if_after.date()}")
    else:
        fetch_if_after = None
        print("Refetching everything")

    mod_dir = "../Chapters"
    if incremental:
        chapter_ids = load_changed_chapters(chapters_file)
        print(f"Incremental mode for {len(chapter_ids)} chapter(s): {chapter_ids}")
        all_chaps = []
        for chapter_id in chapter_ids:
            chap_meta = chapter_meta_for_id(mod_dir, chapter_id, config)
            if chap_meta is not None:
                all_chaps.append(chap_meta)
    else:
        print("Reading metadata for all books")
        all_chaps = chapter_metas_for_all_books(mod_dir, config)

    # In incremental mode we preserve existing links and update just what changed.
    # In full mode we rebuild the dictionary from chapter metadata.
    new_links = dict(old_links) if incremental else {}

    broken_links = []
    for chap_meta in all_chaps:
        urls = util.urls_in_chapter_meta(chap_meta)
        if not urls:
            continue

        print(f"Chapter: {chap_meta['id']} ({chap_meta['title']})...")
        for url in urls:
            if fetch_if_after is not None and url in old_links:
                link_data = old_links[url]
                if "date" in link_data:
                    old_fetch = datetime.datetime.fromisoformat(link_data["date"])
                    if old_fetch > fetch_if_after:
                        new_links[url] = link_data
                        print(f"\tSkipping {url}: Cached {link_data['date']}")
                        continue

            print(f"\tFetching {url}:", end="", flush=True)
            try:
                title = fetch_title_for_url(url)
            except urllib.error.HTTPError as e:
                print(
                    f"\n\tError for {chap_meta['id']} {url}: "
                    f"The server couldn't fulfill the request. Error code: {e.code}"
                )
                broken_links.append({"chap_id": chap_meta["id"], "url": url, "error": e.code})
                continue
            except urllib.error.URLError as e:
                print(f"\n\tError for {url}: Failed to reach server. Reason: {e.reason}")
                continue
            except Exception as e:
                print(f"\n\tError fetching {url}: {e}")
                continue

            new_links[url] = {"title": title, "date": now_str}
            if title == url:
                print("(no title found)")
            else:
                print(f"\"{title}\"")

    with open(linkpath, "w", encoding="utf-8") as f:
        json.dump(new_links, f, indent=2)

    print(f"Done. Saved in {linkpath}")

    if broken_links:
        print("Broken links:")
        for link in broken_links:
            print(f"{link['chap_id']}, Error {link['error']}, {link['url']}")


if __name__ == "__main__":
    main()
