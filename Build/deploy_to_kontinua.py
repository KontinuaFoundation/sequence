'''
PLEASE READ THE README.rst in root/Build BEFORE RUNNING TO understand what this script does!
'''

import subprocess
import os
from pathlib import Path

URL_CHECK_DAYS = 90

BUILD_DIR = Path(__file__).resolve().parent

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

def run_helper_scripts_parallel(BUILD, URL_CHECK_ARG):
    """Runs listed scripts to assist in building of Kontinua PDF web viewer, "The state of things". 
    runs: 
    `url_check.py`
    
    `gather_resources.py`
    
    `make_chapter_pdfs.py`
    
    `build_chapterlist.py`

    Attempts to run scripts in parallel
    Args:
        BUILD (_type_): a string of the build directory
        URL_CHECK_ARG (_type_): _description_
    """
    # consecutive
    run(["python3", "url_check.py", str(URL_CHECK_ARG)], cwd=str(BUILD))
    run(["python3", "gather_resources.py"], cwd=str(BUILD))
    # FIXME gather needed?
    
    # parallel 
    run_parallel([
        ["python3", "make_chapter_pdfs.py", "en_US"],
        ["python3", "build_chapterlist.py"],
    ], cwd=str(BUILD))
    print("====================================")
    print("finished running helper scripts.")
    print("====================================")

def run_bash_script(BUILD, filename: str):
    """Run a generic bash script

    Args:
        BUILD (str): the build directory (current as this script)
        filename (str): the name of bash script
    """
    print("====================================")
    print(f'Running {filename} in:', BUILD)
    print("====================================")
    subprocess.run(
        ["bash", filename],
        cwd=str(BUILD),
        check=True
    )

# run_helper_scripts_parallel(BUILD=BUILD_DIR, URL_CHECK_ARG=URL_CHECK_DAYS) 
run_bash_script(BUILD=BUILD_DIR, filename="concat_chaps.bash")
run_bash_script(BUILD=BUILD_DIR, filename="deploy.bash")

