import json
from pathlib import Path

import util

chap_file = Path("student.tex")
CURRENT_CHAPTER_DIR = Path.cwd()
ROOT_DIR = CURRENT_CHAPTER_DIR.parent.parent.parent
BUILD_DIR  = ROOT_DIR / "Build"

workdir = Path("../../../Build/Intermediate")

workdir.mkdir(parents=True, exist_ok=True)

with open(BUILD_DIR / "user.cfg", "r") as f:
    config = json.load(f)

print(f"Building {chap_file} (in {CURRENT_CHAPTER_DIR})")
final_pdf_path = CURRENT_CHAPTER_DIR / "student.pdf"

util.build_chapter(str(chap_file), str(CURRENT_CHAPTER_DIR), config, str(final_pdf_path))