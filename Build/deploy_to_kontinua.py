'''
PLEASE READ THE README.rst in root/Build BEFORE RUNNING TO understand what this script does!
'''

import subprocess
import os
import sys
from pathlib import Path

URL_CHECK_DAYS = 90

BUILD_DIR = Path(__file__).resolve().parent

def usage(exit_code=0):
    print(
        "deploy_to_kontinua.py: Runs a sequence of functions to prepare and transfer files to the kontinuafoundation.github.io page website for live view."
        "Usage:\n"
        "  python3 build_all.py [--force]\n\n"
        "Options:\n"
        "  --force    Force rebuild of chapter PDFs (disables date checks)\n"
    )
    sys.exit(exit_code)

VALID_ARGS = {"--force", "--help", "-h"}

args = sys.argv[1:]

# Reject unknown args
for arg in args:
    if arg not in VALID_ARGS:
        print(f"Unknown argument: {arg}\n")
        usage(1)

# Handle help
if "--help" in args or "-h" in args:
    usage(0)

# Reject too many args
if len(args) > 1:
    print("Too many arguments.\n")
    usage(1)

# Detect --force

FORCE = "--force" in sys.argv
if FORCE:
    sys.argv.remove("--force")

def run(cmd, cwd):
    print("> " + " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)

def run_parallel(cmds, cwd):
    procs = []
    for cmd in cmds:
        print("> (parallel) " + " ".join(cmd))
        procs.append(subprocess.Popen(cmd, cwd=cwd))
    # wait for all, fail if any failed
    for p in procs:
        rc = p.wait()
        if rc != 0:
            raise RuntimeError(f"A parallel command failed with exit code {rc}")

def run_helper_scripts_parallel(BUILD, URL_CHECK_ARG, FORCE=False):
    """Runs listed scripts to assist in building of Kontinua PDF web viewer."""

    # consecutive
    run(["python3", "url_check.py", str(URL_CHECK_ARG)], cwd=str(BUILD))
    run(["python3", "gather_resources.py"], cwd=str(BUILD))
    # FIXME gather needed?


    # if force tag is given, passes force tag to make_chapter_pdfs.py
    make_chapters_cmd = ["python3", "make_chapter_pdfs.py", "en_US"]
    if FORCE:
        make_chapters_cmd.append("--force")

    # parallel
    run_parallel([
        make_chapters_cmd,
        ["python3", "build_chapterlist.py"],
    ], cwd=str(BUILD))

    print("====================================")
    print("finished running helper scripts.")
    print("====================================")

def run_bash_script(BUILD, filename: str):
    """Run a generic bash script"""
    print("====================================")
    print(f'Running {filename} in:', BUILD)
    print("====================================")
    subprocess.run(
        ["bash", filename],
        cwd=str(BUILD),
        check=True
    )

# -----------------------------
# pass FORCE through
# -----------------------------
run_helper_scripts_parallel(
    BUILD=BUILD_DIR,
    URL_CHECK_ARG=URL_CHECK_DAYS,
    FORCE=FORCE,
)
run_bash_script(BUILD=BUILD_DIR, filename="concat_chaps.bash")
run_bash_script(BUILD=BUILD_DIR, filename="deploy.bash")
