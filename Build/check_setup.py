#!/usr/bin/env python3
"""Check that this computer has everything needed to build the Kontinua books.

Run it after cloning the repository, and again whenever a build fails in a way
you do not understand:

    python3 Build/check_setup.py           # check everything, including a test build
    python3 Build/check_setup.py --fix     # also fix the problems it can fix
    python3 Build/check_setup.py --quick   # skip the test build

It checks Python, the build configuration (user.cfg), LuaLaTeX, every LaTeX
package and font that Support/ourbook.cls uses, the minted code highlighter,
and the tools contributors need. Finally, it builds a small test document with
the real class. For each problem, it prints what is wrong and how to fix it.

With --fix, it asks whether you print on Letter or A4 paper and saves the answer
in user.cfg (creating the file if it is missing), downloads and installs
missing Google fonts for your user account (macOS and Linux), and, if minted's
helper program does not work with your Python, installs a small wrapper that
runs it with an older Python.

The exit status is 0 if the books can be built and 1 if something required is
missing.
"""

import argparse
import importlib.metadata
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

BUILD_DIR = Path(__file__).resolve().parent
SUPPORT_DIR = BUILD_DIR / "Support"
CLASS_FILE = SUPPORT_DIR / "ourbook.cls"
USER_CFG = BUILD_DIR / "user.cfg"
DEFAULT_CFG = SUPPORT_DIR / "default.cfg"

# The LaTeX packages and fonts are read from ourbook.cls. These tables only say
# where to get each one when it is missing.

# .sty file -> TeX Live package that provides it (when the names differ)
TEX_PACKAGE_FOR = {
    "algorithm": "algorithms", "algpseudocode": "algorithmicx",
    "amsthm": "amscls", "amssymb": "amsfonts", "graphicx": "graphics",
    "multicol": "tools", "subcaption": "caption", "tikz": "pgf",
}

GOOGLE = "https://github.com/google/fonts/raw/main/ofl/"
OPEN_SANS = "https://github.com/googlefonts/opensans/raw/main/fonts/ttf/"
# font name used in the class -> files to download
FONT_DOWNLOADS = {
    "Marcellus-Regular": [GOOGLE + "marcellus/Marcellus-Regular.ttf"],
    "MarcellusSC-Regular": [GOOGLE + "marcellussc/MarcellusSC-Regular.ttf"],
    "Inconsolata": [GOOGLE + "inconsolata/static/Inconsolata-Regular.ttf"],
    "Inconsolata-Bold": [GOOGLE + "inconsolata/static/Inconsolata-Bold.ttf"],
    "OpenSans-Regular": [OPEN_SANS + "OpenSans-Regular.ttf"],
    "OpenSans-SemiBold": [OPEN_SANS + "OpenSans-SemiBold.ttf"],
    "OpenSans-Bold": [OPEN_SANS + "OpenSans-Bold.ttf"],
    "OpenSans-BoldItalic": [OPEN_SANS + "OpenSans-BoldItalic.ttf"],
}
FONT_PAGES = {
    "Marcellus": "https://fonts.google.com/specimen/Marcellus",
    "MarcellusSC": "https://fonts.google.com/specimen/Marcellus+SC",
    "Inconsolata": "https://fonts.google.com/specimen/Inconsolata",
    "OpenSans": "https://fonts.google.com/specimen/Open+Sans",
}

MIN_PYTHON = (3, 10)
MIN_TEXLIVE_YEAR = 2023
OLDER_PYTHONS = ["python3.13", "python3.12", "python3.11", "python3.10"]


# ---------------------------------------------------------------- reporting

USE_COLOR = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None
COLORS = {"ok": "\033[92m", "warn": "\033[93m", "fail": "\033[91m", "fixed": "\033[96m"}
LABELS = {"ok": "  ok  ", "warn": " warn ", "fail": " FAIL ", "fixed": "FIXED "}
results = []


def report(status, message, fix=None):
    """Print one result. status is 'ok', 'warn', 'fail', or 'fixed'."""
    results.append(status)
    label = LABELS[status]
    if USE_COLOR:
        label = f"{COLORS[status]}{label}\033[0m"
    print(f"[{label}] {message}")
    if fix:
        for line in fix.strip().splitlines():
            print(f"         {line}")


def heading(title):
    print(f"\n{title}\n{'-' * len(title)}")


def run(cmd, timeout=60, cwd=None):
    """Run a command and return (exit code, combined output). Missing programs give code 127."""
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=cwd)
        return p.returncode, (p.stdout or "") + (p.stderr or "")
    except FileNotFoundError:
        return 127, ""
    except subprocess.TimeoutExpired:
        return 124, "timed out"


# ---------------------------------------------------------------- checks

def check_python():
    heading("Python")
    version = ".".join(map(str, sys.version_info[:3]))
    if sys.version_info[:2] >= MIN_PYTHON:
        report("ok", f"Python {version} ({sys.executable})")
    else:
        report("fail", f"Python {version} is too old; the build scripts need {MIN_PYTHON[0]}.{MIN_PYTHON[1]} or later.",
               "Install a newer Python from https://www.python.org/downloads/ (or `brew install python@3.13`).")

    # Libraries for the web-resource scripts
    missing, mismatched = [], []
    for line in (BUILD_DIR / "requirements.txt").read_text().splitlines():
        line = line.split("#")[0].strip()
        if not line:
            continue
        name, _, wanted = line.partition("==")
        try:
            have = importlib.metadata.version(name)
            if wanted and have != wanted:
                mismatched.append(f"{name} {have} (requirements.txt says {wanted})")
        except importlib.metadata.PackageNotFoundError:
            missing.append(name)
    if missing:
        report("warn", "Python libraries for the web-resource scripts are missing: " + ", ".join(missing)
               + ". (The PDFs build without them.)",
               "pip3 install -r Build/requirements.txt")
    elif mismatched:
        report("ok", "Python libraries are installed; some versions differ from requirements.txt: "
               + "; ".join(mismatched))
    else:
        report("ok", "Python libraries for the web-resource scripts are installed")


PAPER_SIZES = ("Letter", "A4")   # must match PAPER_OPTIONS in util.py


def ask_paper(current):
    """Ask which paper size to use. Returns the answer, or the current value if no one can answer."""
    if not sys.stdin.isatty():
        return None
    answers = {"l": "Letter", "letter": "Letter", "a": "A4", "a4": "A4"}
    while True:
        try:
            reply = input(f"         Which paper size should the books use: [L]etter or [A]4? "
                          f"(press Enter to keep {current}) ").strip().lower()
        except EOFError:
            return None
        if not reply:
            return current
        if reply in answers:
            return answers[reply]
        print("         Please type L for Letter or A for A4.")


def choose_paper(cfg, created):
    """With --fix: ask for the paper size and save it in user.cfg."""
    current = cfg.get("Paper") if cfg.get("Paper") in PAPER_SIZES else "Letter"
    choice = ask_paper(current)
    if choice is None:
        report("warn", f"Not asking for a paper size (this is not an interactive terminal); using {current}.",
               f"To change it, edit \"Paper\" in {USER_CFG} (\"Letter\" or \"A4\").")
        choice = current
    if choice != cfg.get("Paper") or created:
        cfg["Paper"] = choice
        USER_CFG.write_text(json.dumps(cfg, indent=4) + "\n")
        report("fixed", f"Paper size set to {choice} in Build/user.cfg")
    return cfg


def check_config(fix):
    heading("Build configuration")
    if not USER_CFG.exists():
        if fix:
            shutil.copyfile(DEFAULT_CFG, USER_CFG)
            report("fixed", f"Created {USER_CFG} from Support/default.cfg")
            return choose_paper(json.loads(USER_CFG.read_text()), created=True)
        else:
            report("warn", "Build/user.cfg does not exist yet. The build scripts create it the first time they run.",
                   "Run this script with --fix to create it now.")
            return json.loads(DEFAULT_CFG.read_text())
    try:
        cfg = json.loads(USER_CFG.read_text())
    except json.JSONDecodeError as error:
        report("fail", f"Build/user.cfg is not valid JSON: {error}",
               "Fix the file, or delete it and run this script with --fix.")
        return json.loads(DEFAULT_CFG.read_text())
    if fix:
        cfg = choose_paper(cfg, created=False)
    missing = [key for key in ("Languages", "Paper", "LatexExecutable") if key not in cfg]
    if cfg.get("Paper") not in PAPER_SIZES and "Paper" not in missing:
        report("fail", f"Paper in Build/user.cfg is {cfg.get('Paper')!r}; it must be \"Letter\" or \"A4\".",
               "Run this script with --fix to choose one.")
    if missing:
        report("fail", f"Build/user.cfg is missing: {', '.join(missing)}",
               "Compare it with Build/Support/default.cfg.")
    else:
        report("ok", f"Build/user.cfg: languages {cfg['Languages']}, paper {cfg['Paper']}, "
               f"LaTeX command {cfg['LatexExecutable']!r}")
    return cfg


def check_latex(cfg):
    """Check LuaLaTeX and its tools. Returns the lualatex path, or None."""
    heading("LuaLaTeX")
    exe = cfg.get("LatexExecutable", "lualatex")
    path = shutil.which(exe) or (exe if Path(exe).exists() else None)
    if not path:
        report("fail", f"Cannot find the LaTeX program {exe!r} (from Build/user.cfg).",
               "Install TeX Live: on a Mac, `brew install mactex-no-gui`; on Windows, MiKTeX;\n"
               "on Linux, your distribution's texlive packages. If it is installed but not on\n"
               "your PATH, put its full path in Build/user.cfg as LatexExecutable.")
        return None
    code, out = run([path, "--version"])
    first = out.splitlines()[0] if out else "unknown version"
    years = [int(y) for y in re.findall(r"(?:TeX Live|MiKTeX)\D*(\d{4})", out)]
    if code != 0:
        report("fail", f"{path} did not run: {first}")
        return None
    if years and years[0] < MIN_TEXLIVE_YEAR:
        report("warn", f"{first}: this TeX installation is old; some packages may be missing or outdated.",
               "Update TeX Live (or MiKTeX) to a recent release.")
    else:
        report("ok", f"{first} ({path})")
    for tool in ("kpsewhich", "luaotfload-tool"):
        if not (shutil.which(tool) or (Path(path).parent / tool).exists()):
            report("fail", f"Cannot find {tool}, which comes with LuaLaTeX.",
                   "Make sure TeX's bin folder is on your PATH.")
    return path


def tex_tool(latex_path, name):
    sibling = Path(latex_path).parent / name
    return str(sibling) if sibling.exists() else (shutil.which(name) or name)


def class_packages():
    text = re.sub(r"(?<!\\)%.*", "", CLASS_FILE.read_text(encoding="utf-8"))
    packages = set()
    for group in re.findall(r"\\(?:usepackage|RequirePackage)(?:\[[^\]]*\])?\{([^}]*)\}", text):
        packages.update(p.strip() for p in group.split(",") if p.strip())
    return sorted(packages)


def check_packages(latex_path):
    heading("LaTeX packages used by ourbook.cls")
    kpsewhich = tex_tool(latex_path, "kpsewhich")
    packages = class_packages()
    missing = [p for p in packages if run([kpsewhich, f"{p}.sty"])[0] != 0]
    if missing:
        names = sorted({TEX_PACKAGE_FOR.get(p, p) for p in missing})
        report("fail", f"Missing LaTeX packages: {', '.join(missing)}",
               "With TeX Live:  tlmgr install " + " ".join(names) + "\n"
               "(MiKTeX installs missing packages automatically the first time they are used.)")
    else:
        report("ok", f"All {len(packages)} packages are installed")


def class_fonts():
    """Font names the class asks for, plus the bold code font."""
    text = re.sub(r"(?<!\\)%.*", "", CLASS_FILE.read_text(encoding="utf-8"))
    names = re.findall(r"\\(?:setmainfont|setmonofont|setsansfont|fontspec)\{([^}]*)\}", text)
    fonts = []
    for name in names:
        name = re.sub(r"\.(ttf|otf)$", "", name)
        if name not in fonts:
            fonts.append(name)
    if "Inconsolata" in fonts and "Inconsolata-Bold" not in fonts:
        fonts.append("Inconsolata-Bold")   # bold code, chosen automatically by fontspec
    return fonts


def font_found(latex_path, name):
    code, out = run([tex_tool(latex_path, "luaotfload-tool"), f"--find={name}"])
    match = re.search(r'Resolved file name "([^"]+)"', out)
    return match.group(1) if match else None


def user_font_dir():
    system = platform.system()
    if system == "Darwin":
        return Path.home() / "Library" / "Fonts"
    if system == "Linux":
        return Path.home() / ".local" / "share" / "fonts"
    return None


def check_fonts(latex_path, fix):
    heading("Fonts used by ourbook.cls")
    missing = []
    for name in class_fonts():
        where = font_found(latex_path, name)
        if where:
            report("ok", f"{name}: {where}")
        else:
            missing.append(name)
    if not missing:
        return
    font_dir = user_font_dir()
    if fix and font_dir:
        font_dir.mkdir(parents=True, exist_ok=True)
        installed = []
        for name in missing:
            for url in FONT_DOWNLOADS.get(name, []):
                target = font_dir / url.rsplit("/", 1)[1]
                try:
                    urllib.request.urlretrieve(url, target)
                    installed.append(name)
                except OSError as error:
                    report("fail", f"Could not download {url}: {error}")
        if shutil.which("fc-cache"):
            run(["fc-cache", "-f", str(font_dir)], timeout=300)
        run([tex_tool(latex_path, "luaotfload-tool"), "--update"], timeout=600)
        for name in missing:
            if font_found(latex_path, name):
                report("fixed", f"{name}: installed in {font_dir}")
            else:
                report("fail", f"{name}: still not found after installing.", _font_help(name))
        return
    for name in missing:
        hint = _font_help(name)
        if font_dir and name in FONT_DOWNLOADS:
            hint += "\nOr run this script with --fix to download and install it for you."
        report("fail", f"{name}: not found", hint)


def _font_help(name):
    if name == "TeX Gyre Pagella":
        return "This font comes with TeX Live (package tex-gyre): tlmgr install tex-gyre"
    family = name.split("-")[0]
    page = FONT_PAGES.get(family, "https://fonts.google.com/")
    return (f"Download it from {page} and install it, then run `luaotfload-tool --update`.")


def check_minted(latex_path, fix):
    heading("Code highlighting (minted)")
    # LuaLaTeX finds latexminted on the PATH, so look it up the same way.
    helper = shutil.which("latexminted") or tex_tool(latex_path, "latexminted")
    code, out = run([helper, "--version"])
    if code == 0:
        report("ok", f"{out.splitlines()[0]} works")
        return
    if code == 127:
        report("fail", "Cannot find latexminted, the helper program the minted package runs.",
               "It comes with TeX Live's minted package: tlmgr install minted")
        return
    # latexminted exists but crashes: usually Python 3.14 or later.
    # Keep the path as found (often a stable symlink) so the wrapper survives TeX Live updates.
    real = Path(helper)
    older = next((p for p in OLDER_PYTHONS if shutil.which(p) and run([p, str(real), "--version"])[0] == 0), None)
    problem = ("latexminted does not run with your default Python, so every code listing would be "
               "printed without syntax highlighting.")
    if not older:
        report("fail", problem,
               "latexminted needs Python 3.13 or earlier. Install one (for example,\n"
               "`brew install python@3.13`) and run this script again with --fix.")
        return
    wrapper_dir = Path.home() / "bin"
    wrapper = wrapper_dir / "latexminted"
    script = f'#!/bin/sh\nexec {older} "{real}" "$@"\n'
    if fix and platform.system() != "Windows":
        wrapper_dir.mkdir(exist_ok=True)
        wrapper.write_text(script)
        wrapper.chmod(0o755)
        if Path(shutil.which("latexminted") or "").resolve() == wrapper.resolve():
            report("fixed", f"Installed {wrapper}, which runs latexminted with {older}")
        else:
            report("warn", f"Installed {wrapper}, which runs latexminted with {older}, but it is not first on your PATH.",
                   f"Add this line to your shell startup file (such as ~/.zshrc), then open a new terminal:\n"
                   f'    export PATH="$HOME/bin:$PATH"')
        return
    report("fail", problem + f" {older} works.",
           f"Create {wrapper} containing:\n"
           + "".join(f"    {line}\n" for line in script.splitlines())
           + f"make it executable (chmod +x {wrapper}), and put ~/bin first on your PATH.\n"
           "Or run this script with --fix to do this for you.")


def check_contributor_tools():
    heading("Tools for contributors (not needed to build)")
    if shutil.which("git"):
        report("ok", "git")
    else:
        report("warn", "git is not installed; you need it to clone the repository and contribute.",
               "Install it from https://git-scm.com/downloads")
    if shutil.which("bun") or shutil.which("npm"):
        report("ok", "bun or npm (for the spell-check git hook)")
    else:
        report("warn", "Neither bun nor npm is installed; the spell-check hook will not run before commits.",
               "Install bun (https://bun.sh) or Node.js, then run `bun install` in the repository.")


TEST_DOCUMENT = r"""\documentclass[11pt,%(paper)s]{%(cls)s}
\begin{document}
\chapter{Setup Check}
Text in Pagella, with \newterm{a new term}, math $\int_0^1 x^2\,dx = \frac{1}{3}$, and a file
name, \filename{check\_setup.py}.
\section{Code}
\begin{minted}{python}
def greet(name):
    return "Hello, " + name  # highlighted?
\end{minted}
\begin{mdframed}[style=important, frametitle={A Box}]
$E = mc^2$
\end{mdframed}
\begin{tikzpicture}\draw[->, sdkblue] (0,0) -- (1,1);\end{tikzpicture}
\begin{Exercise}[title={A Test}, label=setup1, space=1cm]
What is $2 + 2$?
\end{Exercise}
\begin{Answer}[ref=setup1]
4
\end{Answer}
\chapter{Answers}
\shipoutAnswer
\end{document}
"""


def test_build(latex_path, cfg):
    heading("Test build")
    paper = {"Letter": "letterpaper", "A4": "a4paper"}.get(cfg.get("Paper"), "letterpaper")
    with tempfile.TemporaryDirectory() as tmp:
        cls = (SUPPORT_DIR / "ourbook").as_posix()
        Path(tmp, "setup_check.tex").write_text(TEST_DOCUMENT % {"cls": cls, "paper": paper}, encoding="utf-8")
        cmd = [latex_path, "--shell-escape", "--interaction=nonstopmode", "setup_check.tex"]
        code, out = run(cmd, timeout=600, cwd=tmp)
        log_path = Path(tmp, "setup_check.log")
        log = log_path.read_text(errors="replace") if log_path.exists() else out
        pdf = Path(tmp, "setup_check.pdf").exists()
        errors = [line for line in log.splitlines() if line.startswith("!")]
        no_highlight = "Cannot highlight code" in log or "minted executable is unavailable" in log
        font_errors = sorted(set(re.findall(r'The font "([^"]+)" cannot be found', log)))
        real_errors = [e for e in errors if "minted" not in e.lower()]
        if pdf and not real_errors and not no_highlight:
            report("ok", f"Built a test document with ourbook.cls on {cfg.get('Paper', 'Letter')} paper: fonts, "
                   "math, highlighted code, TikZ, boxes, and an exercise with its answer")
            return True
        if font_errors:
            report("fail", "The test build could not find these fonts: " + ", ".join(font_errors))
        if no_highlight:
            report("fail", "The test build worked, but minted could not highlight code (see above).")
        if real_errors:
            report("fail", "The test build stopped with LaTeX errors:",
                   "\n".join(real_errors[:5]) + "\nTo see the full log, build a chapter with build_chapter.py.")
        if not pdf and not real_errors:
            report("fail", "The test build did not produce a PDF.", (out or "")[-600:])
        return False


# ---------------------------------------------------------------- main

def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--fix", action="store_true",
                        help="fix what can be fixed: choose Letter or A4 paper and save it in user.cfg, install missing fonts, "
                             "install a latexminted wrapper")
    parser.add_argument("--quick", action="store_true", help="skip the test build")
    args = parser.parse_args()

    print("Checking whether this computer can build the Kontinua books...")
    check_python()
    cfg = check_config(args.fix)
    latex = check_latex(cfg)
    if latex:
        check_packages(latex)
        check_fonts(latex, args.fix)
        check_minted(latex, args.fix)
    check_contributor_tools()
    if latex and not args.quick:
        test_build(latex, cfg)

    failures, warnings = results.count("fail"), results.count("warn")
    print()
    if failures:
        print(f"{failures} problem(s) to fix: the books will not build, or will build incorrectly"
              + (f" ({warnings} warning(s) as well)." if warnings else "."))
        if not args.fix:
            print("Some can be fixed automatically: python3 Build/check_setup.py --fix")
        return 1
    print("Ready to build" + (f" ({warnings} warning(s) above)." if warnings else ".")
          + " Next: cd Build && python3 build_workbook.py 1")
    return 0


if __name__ == "__main__":
    sys.exit(main())
