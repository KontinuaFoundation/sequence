import json
import os
import shutil
import sys
import argparse
from pathlib import Path
from enum import Enum
import time
from datetime import datetime

import util

mod_dir = "../../Chapters"
VOL_COUNT = 36
MAX_PASSES = 4
STABILITY_EXTNS = [".aux", ".toc", ".out", ".idx"]

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
#        f"  <i>   required, the integer number of the workbook to build between 00-{VOL_COUNT}.\n"
#        f"        Alternatively, python3 build_workbook.py all\n"
#         "OR\n"
#         "Usage:\n"
#         "  python3 build_workbook.py --chapters <chapters>\n"
#         "  --chapters   Enables custom workbook build. Must be followed by chapter ids separated by commas\n"
#         "  python3 build_workbook.py --chapters circles,circular,circular_2,oscillations"
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

def _aux_state(jobname):
    state = {}
    for ext in STABILITY_EXTNS:
        path = INTERMEDIATE_DIR / f"{jobname}{ext}"
        if path.exists():
            state[ext] = path.read_bytes()
        else:
            state[ext] = None
    return state

# Pass 1: the files go from nothing to something, but pass 1 is below min_passes (2), so it continues.
# Pass 2: the .toc page numbers change, so it continues.
# Pass 3: nothing changes, so it stops after 3 passes.
def run_latex_passes(cmd, log_f, jobname, prefix, min_passes, max_passes=MAX_PASSES):
    passes = 0
    while True:
        # 1. snapshot the 4 aux files
        before = _aux_state(jobname)
        # 2. run LaTeX
        rc = util.run_with_spinner(cmd, INTERMEDIATE_DIR, log_f, prefix=prefix,
                                   current=passes, total=max(3, passes + 1))
        passes += 1
        # 3. LaTeX failed: stop, report failure
        if rc != 0:                                    
            print()
            return passes, False
         # 4. safety cap
        if passes >= max_passes:                      
            break
        if passes >= min_passes and _aux_state(jobname) == before:   # 5. nothing changed: done
            break
    util.print_progress_bar(passes, passes, prefix=prefix)
    return passes, True



def build_book(book_id, config, draft, final_dir, header, footer):
    locale_list = config["Languages"]
    tool = config["LatexExecutable"]

    output_tex_file = INTERMEDIATE_DIR / f"workbook-{book_id}.tex"
    output_pdf_file = INTERMEDIATE_DIR / f"workbook-{book_id}.pdf"
    final_pdf_path = final_dir / output_pdf_file.name

    if final_pdf_path.exists():
        final_pdf_path.unlink()

    chapter_ids, chapter_paths = util.dir_list_for_book(CHAPTERS_DIR, book_id, locale_list)

    with output_tex_file.open("w") as out:
        out.write(header)
        for chapter, path in zip(chapter_ids, chapter_paths):
            if not chapter:
                continue
            out.write(f"\\graphicspath{{{{{Path(path).as_posix()}/}}}}\n")
            out.write(f"\\input{{{(Path(path) / 'student.tex').as_posix()}}}\n")
        out.write(footer)

    log_path = INTERMEDIATE_DIR / f"workbook-{book_id}.log"
    prefix = f"Building workbook-{book_id}"

    cmd = [tool, "-halt-on-error", "-synctex=1", "-shell-escape", output_tex_file.name]

    with log_path.open("w") as log_f:
        if draft:
            passes, ok = run_latex_passes(cmd, log_f, output_tex_file.stem, prefix, min_passes=1, max_passes=1)
        else:
            passes, ok = run_latex_passes(cmd, log_f, output_tex_file.stem, prefix, min_passes=2)

        if not ok or not output_pdf_file.exists():
            print(f"Build failed for {final_pdf_path} (see {log_path} for details)")
            util.print_separator(success=False)
            return None

        if not draft:
            shutil.move(output_pdf_file, final_pdf_path)
            page_count = util.page_count_from_log(log_path)
            page_str = f"{page_count} pages" if page_count is not None else "unknown page count"
            print(f"{final_pdf_path} built ({page_str}).")

    util.print_separator(success=True)
    return final_pdf_path


def main():
    args = parse_args()
    mode= None
    # for if one wants to build a custom workbook with specific chapters, 
    # or if one wants to build a numbered workbook with a specific index
    # called by --chapters <comma-separated list of chapters>
    
    if args.chapters:
        mode = Mode("custom")
        chapters = [c.strip() for c in args.chapters.split(",")]
        print(f"Building custom workbook with: {chapters}")
        for c in chapters:
            if not Path(CHAPTERS_DIR / c / "en_US").exists(): # FIXME en_US hardcoded
                print(f"Invalid chapter: {c}")
                sys.exit(1)
        
    if not args.index and not args.chapters:
        print("Error: must provide an index or --chapters")
        sys.exit(1)
        
    if args.index:
        mode = Mode("numbered")

        if args.index == "all":
            book_nums = ["00"] + [str(x).zfill(2) for x in range(1, VOL_COUNT + 1)]
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
        print("BUILD_DIR:", BUILD_DIR)
        print("ROOT_DIR:", ROOT_DIR)
        print("CHAPTERS_DIR:", CHAPTERS_DIR)
        print("INTERMEDIATE_DIR:", INTERMEDIATE_DIR)
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
            print("\n**** Failures: ****")
            for book in failednumbers:
                log_path = INTERMEDIATE_DIR / f"workbook-{book}.log"
                print(f"  workbook-{book} (see {log_path} for details)")
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

        log_path = INTERMEDIATE_DIR / f"{output_tex.stem}.log"
        prefix = f"Building {output_tex.stem}"

        cmd = [config["LatexExecutable"], "-halt-on-error", "-synctex=1", "-shell-escape", str(output_tex)]

        with log_path.open("w") as log_f:
            _passes, ok = run_latex_passes(cmd, log_f, output_tex.stem, prefix, min_passes=2)

            if not ok or not output_pdf.exists():
                print(f"Build failed for {final_file} (see {log_path} for details)")
                util.print_separator(success=False)
                sys.exit(1)

        shutil.move(output_pdf, final_file)
        page_count = util.page_count_from_log(log_path)
        page_str = f"{page_count} pages" if page_count is not None else "unknown page count"
        print(f"{final_file} built ({page_str}).")
        util.print_separator(success=True)

        print(f"\nCreated:\n{final_file}")
        print("Containing:\n")
        print("\n".join(f" {c}" for c in chapters))
        print("\n")
if __name__ == "__main__":
    start = datetime.now()
    t0 = time.perf_counter()
    print(f"Start: {start:%Y-%m-%d %H:%M:%S}")
    try:
        main()
    finally:
        print(f"End:   {datetime.now():%Y-%m-%d %H:%M:%S} ({time.perf_counter() - t0:.2f} s)")
