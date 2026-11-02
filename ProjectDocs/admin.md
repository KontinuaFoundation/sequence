# Administration

Notes for the people who maintain the repository and publish the workbooks. The
scripts mentioned here are in the `Build` directory and are described in detail in
[`Build/README.rst`](../Build/README.rst).

## Publishing to the website

Publishing to [kontinuafoundation.github.io](https://kontinuafoundation.github.io/)
is automatic. There is nothing to run by hand.

* **On every push** (`.github/workflows/ci.yml`), CI spell-checks the changes,
  rebuilds the chapters and workbooks that changed, checks their links with
  `gather_resources.py`, and regenerates `workbooks.json` and the chapter graph.
  Changes on `master` are published to the site.
* **Every Monday at 06:00 UTC** (`.github/workflows/deploy.yml`), a full deploy
  rebuilds every chapter PDF and every workbook. You can also start a full deploy
  at any time from the **Actions** tab on GitHub: choose **Full Deploy**, then
  **Run workflow**.

## Releasing workbooks to the readers site

To publish a collection to [readers.kontinua.org](https://readers.kontinua.org),
build the Letter-size workbooks, gather the chapter information, and upload them:

```sh
cd Build
python3 build_workbook.py all
python3 gather_resources.py
python3 gather_ebook_resources.py
python3 upload_collection.py
```

`upload_collection.py` asks for a username, locale and version number. See
[Releases](releases.md) for how versions are numbered.

## Keeping the lists of chapters in sync

`Chapters/book_00.txt` lists every chapter of the sequence, in order. It must be
the `book_01.txt` through `book_36.txt` files joined together. After you add,
remove or move a chapter, rebuild `book_00.txt`, check the order of
prerequisites, and regenerate the outline:

```sh
cd Chapters
cat book_{01..36}.txt > book_00.txt
cd ../Build
python3 check_ordering.py
python3 make_outline.py
```

Every `book_NN.txt` must end with a newline. Otherwise `cat` joins the last
chapter of one book to the first chapter of the next.

`make_outline.py` regenerates [the outline](outline.md) from the book lists and
the chapters' `\chapter` and `\section` titles.
