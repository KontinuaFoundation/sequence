import json
import os
import shutil
import subprocess
import sys

import util

mod_dir = "../../Chapters"
vol_count = 36


def usage():
    print("Usage: python3 build_workbook.py <i>")
    print("   or  python3 build_workbook.py all")
    sys.exit(1)


def _run_latex(tool, tex_file):
    return subprocess.run(
        [tool, "-halt-on-error", "-synctex=1", "-shell-escape", tex_file]
    ).returncode


def build_book(book_id, config, draft, final_dir, header, footer):
    locale_list = config["Languages"]
    tool = config["LatexExecutable"]

    output_tex_file = f"workbook-{book_id}.tex"
    output_pdf_file = f"workbook-{book_id}.pdf"
    final_pdf_path = f"../{final_dir}/{output_pdf_file}"
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
    if not os.path.exists("user.cfg"):
        shutil.copyfile("Support/default.cfg", "user.cfg")

    with open("user.cfg", "r") as f:
        config = json.load(f)

    if len(sys.argv) < 2:
        usage()

    final_dir = f"Workbooks-{config['Languages'][0]}-{config['Paper']}"

    for d in ("Intermediate", final_dir):
        os.makedirs(d, exist_ok=True)

    arg1 = sys.argv[1]
    if arg1 == "all":
        book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]
    else:
        book_nums = [arg1.zfill(2)]

    # Cache header/footer once — same for every book.
    with open("Support/bookheader.tex", "r") as f:
        header = f.read()
    with open("Support/bookfooter.tex", "r") as f:
        footer = f.read()

    os.chdir("Intermediate")

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
            print(f"{final_dir}/{filename}")

    if failednumbers:
        print(f"**** Failures: {failednumbers} *****")
        sys.exit(1)


if __name__ == "__main__":
    main()
