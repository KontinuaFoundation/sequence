import csv
import os
import re

base_dir = os.path.join(os.path.dirname(__file__), "..", "Chapters")
book_txt_path = os.path.join(base_dir, "book_00.txt")
csv_file_path = os.path.join(os.path.dirname(__file__), "PNG_Usage_Status.csv")

include_graphics_re = re.compile(r"\\includegraphics(?:\[.*\])?\{(.+?)\}")


def read_chapter_names(path):
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]


chapter_names = read_chapter_names(book_txt_path)

with open(csv_file_path, mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["#-chapter", "filename", "status"])

    for chapter_number, chapter_name in enumerate(chapter_names, start=1):
        chapter_path = os.path.join(base_dir, chapter_name, "en_US")
        if not os.path.isdir(chapter_path):
            continue

        all_pngs = {
            f: 0 for f in os.listdir(chapter_path) if f.endswith(".png")
        }

        for file in os.listdir(chapter_path):
            if not file.endswith(".tex"):
                continue
            with open(os.path.join(chapter_path, file), "r") as tex_file:
                for match in include_graphics_re.findall(tex_file.read()):
                    referenced = os.path.basename(match)
                    if referenced in all_pngs:
                        all_pngs[referenced] = 1

        for filename, status in all_pngs.items():
            writer.writerow([f"{chapter_number}-{chapter_name}", filename, status])

print(f"PNG usage status has been written to: {csv_file_path}")
