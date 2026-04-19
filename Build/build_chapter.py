import json
import os

import util

chap_file = "student.tex"
chap_dir = os.getcwd().replace("\\", "/")
workdir = "../../../Build/Intermediate"

os.makedirs(workdir, exist_ok=True)
os.chdir(workdir)

with open("../user.cfg", "r") as f:
    config = json.load(f)

print(f"Building {chap_file} (in {chap_dir})")
final_pdf_path = f"{chap_dir}/student.pdf"
util.build_chapter(chap_file, chap_dir, config, final_pdf_path)
