import glob
import os
import pathlib
import shutil

dirs = ["Intermediate", *glob.glob("Resources-*"), *glob.glob("Workbooks-*")]
for d in dirs:
    if os.path.exists(d):
        shutil.rmtree(d)

for draft_file in glob.glob("../Chapters/*/*/student.pdf"):
    os.remove(draft_file)

for p in pathlib.Path("../Chapters").rglob("__pycache__"):
    shutil.rmtree(p)

print("Cleaned.")
