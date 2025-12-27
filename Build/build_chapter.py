import json
import os

import util

chap_file = "student.tex"
chap_dir = os.getcwd()
chap_dir = chap_dir.replace("\\", "/")
workdir = "../../../Build/Intermediate"
if not os.path.exists(workdir):
    os.mkdir(workdir)
os.chdir(workdir)

with open("../user.cfg", "r") as config_fd:
    config = json.load(config_fd)

print(f"Building {chap_file} (in {chap_dir})")
final_pdf_path = chap_dir + "/student.pdf"
util.build_chapter(chap_file, chap_dir, config, final_pdf_path)
