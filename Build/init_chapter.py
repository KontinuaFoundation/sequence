# this script is meant to create a new directory arg/en_US, and the corresponding empty digital resource, and emtpy tex file except for \chapter{arg}

# run from the build directory
import argparse
from pathlib import Path

BUILD_DIR = Path.cwd()
ROOT_DIR = BUILD_DIR.parent
CHAPTERS_DIR = ROOT_DIR / "Chapters"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Scaffold a new chapter directory with an empty student.tex and digital_resources.json."
    )
    parser.add_argument("chapter_id", help="Chapter id (ie. hash_tables), used as the directory name.")
    return parser.parse_args()


def init_chapter(chapter_id):
    chapter_dir = CHAPTERS_DIR / chapter_id / "en_US"

    if chapter_dir.exists():
        print(f"Error: {chapter_dir} already exists")
        return False

    chapter_dir.mkdir(parents=True)

    digital_resources = (
        "{\n"
        '  "requires" : [\n'
        "\n"
        "  ],\n"
        '  "files" : [\n'
        "\n"
        "  ],\n"
        '  "covers" : [\n'
        "  ]\n"
        "}\n"
    )
    (chapter_dir / "digital_resources.json").write_text(digital_resources)
    (chapter_dir / "student.tex").write_text(f"\\chapter{{{chapter_id}}}\n")

    print(f"Created {chapter_dir}")
    return True


if __name__ == "__main__":
    args = parse_args()
    init_chapter(args.chapter_id)
