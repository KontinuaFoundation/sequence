import json
import os
import shutil
import subprocess
import sys
import argparse
from pathlib import Path
from enum import Enum
import time

import util

mod_dir = "../../Chapters"
VOL_COUNT = 36

BUILD_DIR = Path.cwd() 
ROOT_DIR = BUILD_DIR.parent
CHAPTERS_DIR = ROOT_DIR / "Chapters"
USR_CFG = BUILD_DIR / "user.cfg"
INTERMEDIATE_DIR = BUILD_DIR / "Intermediate"   


class Mode(str, Enum):
    NUMBERED = "numbered"
    CUSTOM = "custom"

# def usage():
#     print(
#         "Usage:\n"
#         "  python3 build_workbook.py <i>\n"
#         "Options:\n"
#        f"  <i>   required, the integer number of the workbook to build between 00-{vol_count}.\n"
#        f"        Alternatively, python3 build_workbook.py all\n"
#         "OR\n"
#         "Usage:\n"
#         "  python3 build_workbook.py --c chapters=\"<chapters>\"\n"
#         "  --c   Enables custom workbook book build. Must be followed by a sequence of chapters separrated by commas\n"
#         "  python3 build_workbook.py --c chapters=circles,circular,circular_2,oscillations"
#     )
#     sys.exit(1)


def parse_args():
    parser = argparse.ArgumentParser(
    description="Build standard or custom workbooks from LaTeX sources."
)

    parser.add_argument(
        "index",
        nargs="?",
        help="Workbook index (ie. 3 or 31), or 'all'"
    )

    parser.add_argument(
        "--chapters",
        type=str,
        help="Comma-separated chapter list for custom workbook"
    )

    return parser.parse_args()


def _run_latex(tool, tex_file):
    return subprocess.run(
        [tool, "-halt-on-error", "-synctex=1", "-shell-escape", tex_file]
    ).returncode


def build_book(book_id, config, draft, final_dir, header, footer):
    locale_list = config["Languages"]
    tool = config["LatexExecutable"]

    output_tex_file = Path(f"workbook-{book_id}.tex")
    output_pdf_file = Path(f"workbook-{book_id}.pdf")
    final_pdf_path = final_dir / output_pdf_file.name
    if os.path.exists(final_pdf_path):
        os.remove(final_pdf_path)

    chapter_ids, chapter_paths = util.dir_list_for_book(mod_dir, book_id, locale_list)

    with open(output_tex_file, "w") as out:
        out.write(header)
        for chapter, path in zip(chapter_ids, chapter_paths):
            if not chapter:
                continue
            out.write(
                f"\\graphicspath{{{{../../Chapters/{chapter}/{locale_list[0]}}}}}\n"
            )
            out.write(f"\\input{{{path}/student.tex}}\n")
        out.write(footer)

    rc = _run_latex(tool, output_tex_file)
    if rc != 0 or not os.path.exists(output_pdf_file):
        print(f"Build failed for {final_pdf_path}")
        return None

    if not draft:
        # Second pass for cross-references.
        _run_latex(tool, output_tex_file)
        shutil.move(output_pdf_file, final_pdf_path)

    return output_pdf_file


def main():
    print(ROOT_DIR)
    args = parse_args()
    mode= None
    if args.chapters:
        mode = Mode("custom")
        chapters = [c.strip() for c in args.chapters.split(",")]
        print(f"Building custom workbook with: {chapters}")
        for c in chapters:
            if not Path(CHAPTERS_DIR / c / "en_US").exists(): # FIXME en_US harcoded
                print(f"Invalid chapter: {c}")
                sys.exit(1)
        
    if not args.index and not args.chapters:
        print("Error: must provide an index or --chapters")
        sys.exit(1)
        
    if args.index:
        mode = Mode("numbered")

        if args.index == "all":
            book_nums = [str(x).zfill(2) for x in range(1, VOL_COUNT + 1)]
            print("Building all workbooks")
        elif args.index.isdigit():
            book_nums = [str(args.index).zfill(2)]
            if int(args.index) > VOL_COUNT:
                print(f"Error: index cannot be greater than the current workbook count of {VOL_COUNT}")
                sys.exit(1)
                print(f"Building workbook #{args.index}")
        else:
            print("Error: index must be an integer or 'all'")
            sys.exit(1)
    
    if not USR_CFG.exists():
        shutil.copyfile("Support/default.cfg", "user.cfg")

    with USR_CFG.open("r") as f:
        config = json.load(f)
        
    # Cache header/footer once — same for every book.
    header = (BUILD_DIR / "Support" / "bookheader.tex").read_text()
    footer = (BUILD_DIR / "Support" / "bookfooter.tex").read_text()
    
    if mode == Mode.NUMBERED:

        final_dir = BUILD_DIR / f"Workbooks-{config['Languages'][0]}-{config['Paper']}"
        for d in (INTERMEDIATE_DIR, final_dir):
            os.makedirs(d, exist_ok=True)

        INTERMEDIATE_DIR.mkdir(exist_ok=True)
        final_dir.mkdir(exist_ok=True)

        newfilenames = []
        failednumbers = []

        for book in book_nums:
            print(f"Building book {book}")
            newfile = build_book(book, config, False, final_dir, header, footer)
            if newfile is None:
                failednumbers.append(book)
            else:
                newfilenames.append(newfile)

        if newfilenames:
            print("\nCreated:")
            for filename in newfilenames:
                print(final_dir / filename)

        if failednumbers:
            print(f"**** Failures: {failednumbers} *****")
            sys.exit(1)
    if mode == Mode.CUSTOM:
        print("Entering Custom Workbook Mode")

        timestamp = int(time.time() * 1000)
        final_dir = BUILD_DIR / "Custom-Workbooks"

        INTERMEDIATE_DIR.mkdir(exist_ok=True)
        final_dir.mkdir(exist_ok=True)

        os.chdir(INTERMEDIATE_DIR)

        output_tex = Path(f"custom-workbook-{timestamp}.tex")
        output_pdf = Path(f"custom-workbook-{timestamp}.pdf")
        final_file = final_dir / output_pdf.name

        with output_tex.open("w") as out:
            out.write(header)

            for c in chapters:
                chap_dir = CHAPTERS_DIR / c / config["Languages"][0]
                out.write(f"\\graphicspath{{{{{chap_dir}}}}}\n")
                out.write(f"\\input{{{chap_dir / 'student.tex'}}}\n")

            out.write(footer)

        rc = _run_latex(config["LatexExecutable"], output_tex)

        if rc != 0 or not output_pdf.exists():
            print(f"Build failed for {final_file}")
            sys.exit(1)

        _run_latex(config["LatexExecutable"], output_tex)
        shutil.move(output_pdf, final_file)

        print(f"\nCreated:\n{final_file}")
        print("Containing:\n")
        print("\n".join(f" {c}" for c in chapters))
        print("\n")
if __name__ == "__main__":
    main()
