import os
import re
import shutil

base_dir = os.path.join(os.path.dirname(__file__), "..", "Chapters")
dest_dir = os.path.join(os.path.dirname(__file__), "..", "Collected_PNGs")
workbook_tex_path = os.path.join(base_dir, "book_00.txt")

os.makedirs(dest_dir, exist_ok=True)

include_graphics_re = re.compile(r"\\includegraphics(?:\[.*\])?\{(.+?)\}")

EXCLUDE = {
    "02-atomic_mass-03 - KA_Mass_Spectroscopy_Zr.png",
    "06-buoyancy-03 - bouy_word_cloud.png",
    "12-stat_spreadsheets-01 - BlankSheet.png",
    "01-matter_energy_intro-04 - KA_Endo.png",
    "02-atomic_mass-01 - periodic.png",
}


def read_chapter_names(path):
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]


chapter_names = read_chapter_names(workbook_tex_path)

for chapter_number, chapter_name in enumerate(chapter_names, start=1):
    chapter_path = os.path.join(base_dir, chapter_name, "en_US")
    if not os.path.isdir(chapter_path):
        continue
    for file in os.listdir(chapter_path):
        if not file.endswith(".tex"):
            continue
        with open(os.path.join(chapter_path, file), "r") as tex_file:
            matches = include_graphics_re.findall(tex_file.read())
        for img_index, match in enumerate(matches, start=1):
            img_filename = os.path.basename(match)
            new_filename = (
                f"{chapter_number:02d}-{chapter_name}-{img_index:02d} - {img_filename}"
            )
            if new_filename in EXCLUDE:
                continue
            img_file_path = os.path.join(chapter_path, match)
            if os.path.exists(img_file_path):
                shutil.copy(img_file_path, os.path.join(dest_dir, new_filename))

print(f"All referenced images have been collected in: {dest_dir}")
