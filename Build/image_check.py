import os
import re

base_dir = os.path.join(os.path.dirname(__file__), "..", "Chapters")
include_graphics_re = re.compile(r"\\includegraphics(?:\[.*\])?\{(.+?)\}")

for root, _, files in os.walk(base_dir):
    if os.path.basename(root) != "en_US":
        continue

    all_pngs = {f for f in files if f.endswith(".png")}
    referenced_pngs = set()

    for file in files:
        if not file.endswith(".tex"):
            continue
        with open(os.path.join(root, file), "r") as tex_file:
            for match in include_graphics_re.findall(tex_file.read()):
                referenced_pngs.add(os.path.basename(match))

    unreferenced = all_pngs - referenced_pngs
    if unreferenced:
        print(f"In {root}, the following PNGs are not referenced in any .tex file:")
        for png in unreferenced:
            print(png)
