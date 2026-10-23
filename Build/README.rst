The Build Directory
===================

This folder contains the scripts that turn the chapters in ``Chapters/`` into
workbook PDFs and web resources, plus the files those scripts need
(``Support/``). The scripts put their products here too: finished workbooks go
in ``Workbooks-<language>-<paper>/`` (for example,
``Workbooks-en_US-Letter/workbook-05.pdf``), and LaTeX's working files go in
``Intermediate/``.

Quick Start
-----------

1. Install the tools and fonts described in "Before You Build" below.
2. Get a copy of the repository (only the latest version, which is much faster
   than downloading its whole history)::

     git clone --depth 1 https://github.com/KontinuaFoundation/sequence.git
     cd sequence

3. Check your setup, and let the checker fix what it can. It also asks whether
   you print on Letter or A4 paper::

     python3 Build/check_setup.py --fix

4. Build a workbook::

     cd Build
     python3 build_workbook.py 1

How the Books Are Organized
---------------------------

* Each chapter is a folder in ``Chapters/``, such as ``Chapters/fluid_flow/``.
  Inside, the ``en_US`` folder holds the chapter text (``student.tex``), its
  images and code files, a ``summary.md``, and ``digital_resources.json``,
  which lists the chapter's downloadable files, the topics it covers
  (``covers``), and the topics it needs first (``requires``).
* ``Chapters/book_01.txt`` through ``book_36.txt`` list the chapters in each
  volume, in order, one chapter folder name per line.
* ``Chapters/book_00.txt`` lists every chapter in the whole series, in reading
  order. It must match the volumes read one after another.
* In any of these lists, a line that starts with ``#`` is ignored. Use that to
  take a chapter out of the books without deleting it (for example,
  ``# economics``).
* The document class that sets the books' design, ``Support/ourbook.cls``, is
  documented in ``Support/README.md``: exercises and answers, boxes, code,
  figures, the index, and more. Read it before writing a chapter.


Before You Build
================

You will need git, Python 3, a full TeX Live installation (which includes
LuaLaTeX), and Node.js.

On a Mac, install Xcode from the App Store (it includes git) and
`Homebrew <https://brew.sh>`_. Then::

  brew install python@3.13
  brew install mactex-no-gui
  brew install node

Clone the GitHub repository::

  git clone --depth 1 https://github.com/KontinuaFoundation/sequence.git

``--depth 1`` downloads only the latest version of the files (about 230 MB)
instead of the repository's entire history (about 1.5 GB). Everything builds the
same way. If you ever need the history, for example to run ``git log`` on old
commits, run ``git fetch --unshallow`` inside the repository. (If you plan to
contribute, clone over SSH instead; see "Contributing" below.)

Fonts
-----

The body text and math fonts (TeX Gyre Pagella and Euler) come with TeX Live.
The other fonts are not ours to redistribute, so they are not in this
repository. Download these from the
`Google Font Collection <https://fonts.google.com/>`_ and install them on your
computer:

* `Marcellus <https://fonts.google.com/specimen/Marcellus>`_ (Regular)
* `Marcellus SC <https://fonts.google.com/specimen/Marcellus+SC>`_ (Regular)
* `Open Sans <https://fonts.google.com/specimen/Open+Sans>`_ (Regular, Semi Bold,
  Bold, and Bold Italic)
* `Inconsolata <https://fonts.google.com/specimen/Inconsolata>`_ (Regular and
  Bold), used for code

On a Mac, double-click each downloaded ``.ttf`` file and click "Install Font".
On Windows, right-click each file and choose "Install for all users". If a
build cannot find a font, LuaLaTeX stops with a "font not found" error; install
the missing font and run ``luaotfload-tool --update`` so LuaLaTeX notices it.

(The CI workflows download Marcellus and Inconsolata from Google's font
repository each time they run, and install Open Sans from Ubuntu's
``fonts-open-sans`` package.)

Python Libraries
----------------

To build the web resources, you will need some Python libraries. Install them
all with::

  pip3 install -r Build/requirements.txt

Python Version and Code Highlighting
------------------------------------

The books use the `minted <https://ctan.org/pkg/minted>`_ package to highlight
code. Minted runs a helper program, ``latexminted``, that comes with TeX Live.
**That helper does not work with Python 3.14 or later** (as of TeX Live 2026,
``latexminted`` 0.6.0). When it fails, the books still build, but every code
listing is printed without syntax highlighting, and each chapter's log shows
``Package minted Error: Cannot highlight code``.

If your ``python3`` is 3.14 or newer, keep Python 3.13 installed (see the
``brew`` command above) and run ``python3 Build/check_setup.py --fix``. It
installs a small script, ``~/bin/latexminted``, that runs ``latexminted`` with
Python 3.13, and tells you if ``~/bin`` needs to be added to the front of your
``PATH``. The script it installs is just::

  #!/bin/sh
  exec python3.13 /opt/homebrew/bin/latexminted "$@"

Check it with ``latexminted --version``, which should print the version
instead of an error.

Checking Your Setup
-------------------

Once everything is installed, run the setup checker from the top of the
repository::

  python3 Build/check_setup.py

It checks, and explains how to fix:

* your Python version, and the Python libraries the web-resource scripts use;
* your ``Build/user.cfg``;
* LuaLaTeX, and every LaTeX package that ``Support/ourbook.cls`` loads (with
  the ``tlmgr install`` command for anything missing);
* every font the class uses;
* minted's ``latexminted`` helper (the Python problem described above);
* git and bun or npm, which you need only to contribute.

Finally, it builds a small test document with the real class (fonts, math,
highlighted code, TikZ, a box, and an exercise with its answer) to prove that
everything works together. This takes about half a minute; ``--quick`` skips
it.

With ``--fix``, it also fixes what it can: it asks whether you print on Letter
or A4 paper and saves your answer in ``user.cfg`` (creating the file if
needed), downloads
and installs any missing Google fonts for your user account (on macOS and
Linux), and installs the ``latexminted`` script described above. It ends with
"Ready to build" (exit status 0) or a count of the problems that remain (exit
status 1).

Run it again whenever a build fails in a way you do not understand.

Windows
-------

A Mac is preferred, but you can build on Windows. In addition to the fonts and
Python libraries above:

* Download and install `MiKTeX <https://miktex.org/download>`_.
* Download and install `Git Bash <https://git-scm.com/downloads>`_.
* Download and install `Python 3.13 <https://www.python.org/downloads/>`_.
* Download and install `Node.js <https://nodejs.org/en>`_.
* Clone the repository, as above.
* If ``lualatex`` is not on your ``PATH``, put its full path in your
  ``user.cfg`` (see "Configuration").
* Run ``python3 Build/check_setup.py``. On Windows, it reports missing fonts
  but cannot install them for you: install them from Google Fonts by hand.


Configuration
=============

The first time you run a build script, it creates ``Build/user.cfg`` by
copying ``Support/default.cfg``. (``create_user_config.py`` also makes one.) It
holds your preferences:

* ``Languages``: the chapter locale folders to use, most preferred first
  (``en_US``).
* ``Paper``: the paper size, ``"Letter"`` or ``"A4"``. The build scripts pass it
  to the class, so it sets the page size of every PDF, and it names the output
  folder (``Workbooks-en_US-A4``). ``check_setup.py --fix`` asks which you
  want.
* ``LatexExecutable``: the LuaLaTeX command. Usually ``lualatex`` works; use a
  full path, such as ``/Library/TeX/texbin/lualatex``, if it is not on your
  ``PATH``.

Please do not commit your ``user.cfg``.


Building
========

All the build scripts run from the ``Build`` directory, except
``build_chapter.py``, which runs from a chapter's folder.

``build_chapter.py``
  Builds just the chapter you are working on, with its answers. Run it from
  the chapter's ``en_US`` folder. The result is ``student.pdf`` in that folder::

    cd Chapters/fluid_flow/en_US
    python3 ../../../Build/build_chapter.py

``build_workbook.py``
  Builds workbook PDFs. Give it a volume number, ``all``, or a custom list of
  chapters::

    python3 build_workbook.py 5
    python3 build_workbook.py all
    python3 build_workbook.py --chapters circular_motion,circular_motion_2,oscillations

``make_chapter_pdfs.py``
  Builds a separate PDF for every chapter. This takes a while::

    python3 make_chapter_pdfs.py en_US

``clean.py``
  Deletes intermediate files and every PDF and HTML file the other scripts
  generate, including the ``student.pdf`` files in chapter folders::

    python3 clean.py


Checking Your Work
==================

``check_ordering.py``
  Checks that every chapter's prerequisites come before it. It reads
  ``Chapters/book_00.txt``, then reads each chapter's
  ``digital_resources.json`` from the first chapter to the last, and reports:

  * chapters with no ``digital_resources.json``,
  * chapters whose ``digital_resources.json`` is not valid JSON,
  * requirements that no chapter covers (when the requirement is the name of
    a chapter rather than a topic id, the report says so), and
  * requirements that are first covered by a *later* chapter, naming that
    chapter, and
  * topic ids that are covered more than once, whether by two chapters or
    twice in the same chapter. Every topic id must be unique; when you find a
    duplicate, keep the id in the chapter that introduces the topic first and
    rename the later one (and update any ``requires`` lists that meant the
    later one).

  A chapter that requires a topic it covers itself is not reported. Each
  chapter is shown with its volume number. Run it from anywhere::

    python3 Build/check_ordering.py

  It prints ``0 problem(s) found.`` and exits with status 0 when everything is
  in order, and exits with status 1 otherwise, so it can also run in CI. Run it
  whenever you add a chapter, move chapters between volumes, or edit a
  ``requires`` or ``covers`` list. Use ``--locale`` to check a locale other
  than ``en_US``.

  When it reports a problem, look at the chapter's text before changing
  anything. Often the metadata is stale and the fix is to edit the ``requires``
  list. Sometimes the chapter really does use something taught later, and the
  fix is to move the chapter, move the material, or explain it where it is
  used.

  Example output::

    Requirements that are first covered by a later chapter: 1
    ---------------------------------------------------------
      projectiles (Vol 7) requires 'quadratic_formula', first covered by solving_quadratics (Vol 8)

    1 problem(s) found.

``make_topic_index.py``
  Writes ``Chapters/topic_index.json`` (used by the KontinuaResourceEditor to
  connect prerequisite topics to chapters) and prints a report of missing
  topics, out-of-order topics, and topics that more than one chapter claims to
  cover. Run it from the ``Build`` folder::

    python3 make_topic_index.py

``check_images.py``
  Lists the PNG files in each chapter folder that no ``.tex`` file uses.
  ``check_images_csv.py`` writes the same information for every chapter in
  ``book_00.txt`` to ``png_usage_status.csv``.

Spell checking
  Your changes are spell-checked automatically before each commit; see
  "Contributing" and "CI" below.


Writing Chapters
================

``init_chapter.py``
  Creates a new chapter folder with an empty ``student.tex`` and
  ``digital_resources.json``::

    python3 init_chapter.py hash_tables

  Then add the chapter to the right ``book_NN.txt`` and to ``book_00.txt``,
  and run ``check_ordering.py``.

``resource_wizard.py``
  Asks questions and fills in a chapter's ``digital_resources.json``. Run it
  from the chapter's ``en_US`` folder::

    python3 ../../../Build/resource_wizard.py


Other Scripts
=============

``gather_resources.py``
  Checks the video and reference URLs in every ``digital_resources.json``,
  looks up each page's title, and writes ``Resources-en_US/Links.json``. It
  skips URLs it confirmed in the last 90 days; give a different number of days
  as an argument, or 0 to recheck everything::

    python3 gather_resources.py
    python3 gather_resources.py 0

``build_workbooks_index.py``
  Builds ``workbooks.json`` in ``Resources-en_US`` from ``Links.json``. Run
  ``gather_resources.py`` first, since it provides the link titles.

``gather_ebook_resources.py``
  Writes ``Resources-en_US/workbook-01.json`` through ``workbook-36.json``, the
  chapter information that ``upload_collection.py`` sends along with each
  volume's PDF. Each file lists the volume's chapters with their ids, titles,
  prerequisites, the page each chapter starts on, and the topics they cover,
  with every video and reference link paired with its title. The list ends with
  two short entries, for the answers and the index, so the ebook reader can put
  them in its table of contents; each has only an id (``answers-04`` and
  ``index-04`` for Volume 4), a title, a chapter number, a starting page, and
  an empty ``covers`` list (the upload server and the reader apps require that
  key). A link with no
  title in ``Links.json`` (usually because the page could not be reached) is
  left out, and the script prints it so you can fix or remove it in the
  chapter's ``digital_resources.json``. Before running it,
  build all 36 volumes (the starting pages come from each volume's ``.toc``
  file in ``Intermediate``) and run ``gather_resources.py`` (the link titles
  come from ``Links.json``)::

    python3 build_workbook.py all
    python3 gather_resources.py
    python3 gather_ebook_resources.py

``build_chapter_list.py``
  Writes ``Resources/chaplist.txt``, the title of every chapter in every book.

``generate_chapter_graph.py``
  Writes ``graph.json``, the chapter dependency graph, to
  ``Workbooks-en_US-Letter``. ``--image`` also draws it as ``graph.png``, and
  ``--recommended`` writes ``Chapters/recommended_book_00.txt``, an order that
  satisfies every prerequisite.

``collect_images.py`` and ``latex_file_proofing.py``
  Copy every image used in the books into ``Collected_PNGs`` and write a LaTeX
  file that shows them all, for proofreading figures in one place.

``structure_sql.py``
  Writes ``sql.txt``, SQL statements that load the volume and chapter
  structure into the website's database.

``upload_collection.py``
  Uploads a finished collection to the readers site
  (``readers.kontinua.org``). It asks for a username, locale, and version
  number. For each volume, it uploads ``Workbooks-en_US-Letter/workbook-NN.pdf``
  and ``Resources-en_US/workbook-NN.json``, so build the Letter PDFs and run
  ``gather_ebook_resources.py`` first.


Contributing
============

If you plan to contribute, set up SSH access to GitHub (see
`GitHub's guide <https://docs.github.com/en/authentication/connecting-to-github-with-ssh>`_),
then clone over SSH::

  git clone --depth 1 git@github.com:KontinuaFoundation/sequence.git

If it asks whether to trust ``github.com``, say yes. A shallow clone like this
can still create branches, commit, push, and open pull requests. It starts with
only the main branch. To work on another branch that is already on GitHub::

  git remote set-branches --add origin <branch>
  git fetch --depth 1 origin <branch>
  git switch <branch>

Run ``git fetch --unshallow`` if you ever need the full history.

Prettier is configured for consistent formatting. To format a ``.tex`` file::

  npx prettier path/to/file.tex --write

This repository also spell-checks your work automatically before every commit.
For that to work, run this once after cloning (and again any time
``package.json`` changes)::

  bun install

(If you do not have ``bun``, install it from `bun.sh <https://bun.sh>`_, or use
``npm install`` instead; either works.) This sets up a git hook that runs
`cspell <https://cspell.org>`_ on your changes right before each commit. See
"CI" below for what to do if it flags something.

Most authors should not commit anything in the ``Build`` directory; they should
work in the ``Chapters`` directory.


CI
==

These scripts run in CI/CD workflows on every commit. A change rebuilds the
affected chapter and its resources and publishes them to
`the live site <https://kontinuafoundation.github.io/>`_.

Spell checking uses `cspell <https://cspell.org>`_ to catch typos before they
reach the live site. It runs in two places: on your machine right before each
commit (through a `husky <https://typicode.github.io/husky/>`_ git hook), and
again in CI on every push and pull request. If either one flags something, the
commit (or CI run) stops and prints the word, file, and line number, so you
know exactly what to fix.

Spell checking sometimes flags words that are correct: code variables, TikZ
internals, people's names, abbreviations, or British spellings. To accept a
word:

1. Open ``project-words.txt`` at the root of the repository (plain text, one
   word per line).
2. Add the word on its own line, roughly alphabetically.
3. Save the file and commit again.

(This replaced the old ``.aspell.en.pws`` and ``codespell`` setup as of July 19,
2026.)


Status
======

All these scripts work, but support for localization is incomplete. When we
start localizing the materials, we will fix that.
