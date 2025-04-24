import os
import sys
import shutil
import json
import util

# Paths are from Intermediate
mod_dir = "../../Chapters"
vol_count = 36

def usage():
    print("Usage: python3 build_workbook.py <i>")
    print("   or  python3 build_workbook.py all")
    sys.exit(1)


def path_for_chapter_locale_list(chapter, locale_list):
    # Assumes mod has already been stripped of whitespace
    # FIXME: When we start localizing, this will need to be smarter
    return f"{mod_dir}/{chapter}/{locale_list[0]}/student.tex"


def build_book(book_id, config, draft, final_dir):
    locale_list = config["Languages"]
    paper_size = config["Paper"]
    tool = config["LatexExecutable"]

    # Where are things going?
    output_tex_file = f"workbook-{book_id}.tex"
    output_pdf_file = f"workbook-{book_id}.pdf"
    final_pdf_path = f"../{final_dir}/{output_pdf_file}"
    if os.path.exists(final_pdf_path):
        os.remove(final_pdf_path)

    # Open the tex file
    output_tex = open(output_tex_file, "w")

    # Write the header
    header_file = open("../Support/bookheader.tex", "r")
    header = header_file.read()
    header_file.close()
    output_tex.write(header)

    # Which modules go into the book?
    (chapter_ids, chapter_paths) =  util.dir_list_for_book(mod_dir, book_id, locale_list)

    for i in range(len(chapter_ids)):
        chapter = chapter_ids[i]
        chapter_path = f"{chapter_paths[i]}/student.tex"
        if len(chapter) > 0:
            # Look for the graphics in the module directory
            gpath_string =f"\\graphicspath{{{{../../Chapters/{chapter}/{locale_list[0]}}}}}\n"
            output_tex.write(gpath_string)

            include_string = "\\input{{{}}}\n".format(chapter_path)
            output_tex.write(include_string)

    # Write the footer
    footer_file = open("../Support/bookfooter.tex", "r")
    footer = footer_file.read()
    footer_file.close()
    output_tex.write(footer)
    output_tex.close()
    os.system(f"{tool} -halt-on-error -synctex=1 {output_tex_file}")

    if not draft:
        # If a pdf was made, run it again to get cross-references right
        if not draft and os.path.exists(output_pdf_file):
            os.system(f"{tool} -halt-on-error -synctex=1 {output_tex_file}")
            shutil.move(output_pdf_file, final_pdf_path)
        else:
            print(f"Build failed for {final_pdf_path}")
            return None

    return output_pdf_file



# If this is the first time, copy the default config
if not os.path.exists("user.cfg"):
    shutil.copyfile("Support/default.cfg", "user.cfg")

# Read the config
with open("user.cfg", "r") as config_fd:
    config = json.load(config_fd)

# Check command line
if len(sys.argv) < 2:
    usage()

final_dir = f"Workbooks-{config['Languages'][0]}-{config['Paper']}"

# Make any directories we need
needed_dirs = ["Intermediate", final_dir]
for dir in needed_dirs:
    if not os.path.exists(dir):
        os.mkdir(dir)

# Deal with first arg
arg1 = sys.argv[1]
if arg1 == "all":
    book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]
else:
    book_nums = [arg1.zfill(2)]

# We build in the Intermediate file
os.chdir("Intermediate")

# Keep track of successes and failures
newfilenames = []
failednumbers = []
for book in book_nums:
    print(f"Building book {book}")
    newfile = build_book(book, config, False, final_dir)
    if newfile is None:
        failednumbers.append(book)
    else:
        newfilenames.append(newfile)

if len(newfilenames) > 0:
    print(f"\nCreated:")
    for filename in newfilenames:
        print(f"{final_dir}/{filename}")

if len(failednumbers) > 0:
    print(f"**** Failures: {failednumbers} *****")
