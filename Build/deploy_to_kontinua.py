"""
PLEASE READ THE README.rst in root/Build BEFORE RUNNING.
"""

import subprocess
import sys
import time
from pathlib import Path

URL_CHECK_DAYS = 90
BUILD_DIR = Path(__file__).resolve().parent
VALID_ARGS = {"--force", "--help", "-h"}


def usage(exit_code=0):
    print(
        "deploy_to_kontinua.py: Runs helper scripts to prepare and transfer files\n"
        "to the kontinuafoundation.github.io site.\n\n"
        "Usage:\n"
        "  python3 deploy_to_kontinua.py [--force]\n\n"
        "Options:\n"
        "  --force    Force rebuild of chapter PDFs (disables date checks)\n"
    )
    sys.exit(exit_code)


def run(cmd, cwd):
    print("> " + " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)


def run_parallel(cmds, cwd):
    procs = [(cmd, subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)) for cmd in cmds]
    for cmd, _ in procs:
        print("> (parallel) " + " ".join(cmd))
    failures = []
    for cmd, p in procs:
        out, _ = p.communicate()
        output = out.decode(errors="replace")
        print(f"--- {' '.join(cmd)} ---\n{output}")
        if p.returncode != 0:
            failures.append((cmd, p.returncode))
    if failures:
        for cmd, rc in failures:
            print(f"FAILED (rc={rc}): {' '.join(cmd)}")
        raise RuntimeError(f"{len(failures)} parallel command(s) failed")


def run_helper_scripts_parallel(build_dir, url_check_days, force=False):
    make_chapters_cmd = ["python3", "make_chapter_pdfs.py", "en_US"]
    if force:
        make_chapters_cmd.append("--force")
    workbook_cmds = [["python3", "build_workbook.py", str(i)] for i in range(1, 37)]

    run_parallel(
        [
            make_chapters_cmd,
            ["python3", "gather_resources.py", str(url_check_days)],
            ["python3", "build_chapterlist.py"],
            *workbook_cmds,
        ],
        cwd=str(build_dir),
    )

    run(["python3", "gather.py"], cwd=str(build_dir))
    run(["python3", "url_check.py"], cwd=str(build_dir))

    print("====================================")
    print("finished running helper scripts.")
    print("====================================")


def run_bash_script(build_dir, filename):
    print("====================================")
    print(f"Running {filename} in: {build_dir}")
    print("====================================")
    subprocess.run(["bash", filename], cwd=str(build_dir), check=True)


def main():
    args = sys.argv[1:]
    for a in args:
        if a not in VALID_ARGS:
            print(f"Unknown argument: {a}\n")
            usage(1)
    if "--help" in args or "-h" in args:
        usage(0)
    if len(args) > 1:
        print("Too many arguments.\n")
        usage(1)

    force = "--force" in args

    start = time.time()
    run_helper_scripts_parallel(BUILD_DIR, URL_CHECK_DAYS, force)
    run_bash_script(BUILD_DIR, "concat_chaps.bash")
    run_bash_script(BUILD_DIR, "copy_resources_to_workbooks.bash")
    run_bash_script(BUILD_DIR, "deploy.bash")
    print("====================================")
    print(f"Elapsed: {time.time() - start:.4f} seconds")
    print("====================================")


if __name__ == "__main__":
    main()
