import json
import os
import re
import shutil
import subprocess

title_pattern = re.compile(r"chapter\{([^\}]+)\}")
chapter_pattern = re.compile(
    r"chapter\}\{\\numberline \{([^\}]+)\}[^\}]+\}\{([0-9]+)\}"
)


def _read(path):
    with open(path, "r") as f:
        return f.read()


def _run_latex(tool, tex_file, extra_args=()):
    cmd = [tool, "-halt-on-error", "-synctex=1", *extra_args, tex_file]
    return subprocess.run(cmd).returncode


def chapter_toc(bookstr):
    toc = {}
    chapter_path = f"Intermediate/workbook-{bookstr}.toc"
    with open(chapter_path) as f:
        for line in f:
            for match in chapter_pattern.finditer(line):
                toc[match.group(1)] = int(match.group(2))
    return toc


def dir_for_id(mod_dir, identifier, langlist):
    # FIXME: should search from favorite to least favorite
    return f"{mod_dir}/{identifier}/{langlist[0]}"


def dir_list_for_book(mod_dir, book_str, langlist):
    # FIXME: should search from favorite to least favorite
    modlist_path = f"{mod_dir}/book_{book_str}.txt"
    if not os.path.exists(modlist_path):
        print(f"Error: Chapter file {modlist_path} doesn't exist")
        return ([], [])

    with open(modlist_path, "r") as f:
        chapters = f.readlines()

    result_paths = []
    result_ids = []
    for chapter in chapters:
        trimmed = chapter.strip()
        if trimmed and not trimmed.startswith("#"):
            print(f"Processing {trimmed}")
            result_ids.append(trimmed)
            result_paths.append(dir_for_id(mod_dir, trimmed, langlist))
        else:
            print(f"Skipping {trimmed}")
    return (result_ids, result_paths)


def title_for_dir(dir):
    fullpath = f"{dir}/student.tex"
    with open(fullpath) as f:
        for line in f:
            match = title_pattern.search(line)
            if match:
                return match.group(1)
    return "UNKNOWN"


def metadata_for_dir(dir):
    rpath = f"{dir}/digital_resources.json"
    if not os.path.exists(rpath):
        print(f"Error: Digital Resources at {rpath} doesn't exist")
        result = {}
    else:
        with open(rpath, "r") as f:
            data = f.read().strip()
        result = json.loads(data) if len(data) >= 2 else {}
    result["title"] = title_for_dir(dir)
    return result


def gather_data(mod_dir, book_str, config):
    (ids, dirs) = dir_list_for_book(mod_dir, book_str, config["Languages"])
    metadatas = []
    topics = {}
    for i, dir in enumerate(dirs):
        md = metadata_for_dir(dir)
        title = title_for_dir(dir)

        md["book"] = book_str
        md["id"] = ids[i]
        md["title"] = title
        md["chap_num"] = i + 1

        if "files" in md:
            for entry in md["files"]:
                entry["link"] = (
                    f"https://github.com/TheKontinua/sequence/raw/master/Chapters/{ids[i]}/en_US/{entry['path']}"
                )
        metadatas.append(md)

        if "covers" in md:
            for c in md["covers"]:
                cd = c.copy()
                cd["book"] = book_str
                cd["chap_title"] = title
                cd["chap_num"] = i + 1
                cd["chap_id"] = ids[i]
                topics[cd["id"]] = cd

    return (metadatas, topics)


def should_build_chapter(tex_path, pdf_path):
    if not os.path.exists(pdf_path):
        return True
    if not os.path.exists(tex_path):
        return True
    return os.path.getmtime(tex_path) > os.path.getmtime(pdf_path)


def build_chapter(chapter_file, chap_dir, config, final_pdf_path, draft=True, date_check=None):
    tex_path = os.path.join(chap_dir, chapter_file)

    if date_check is not None and not should_build_chapter(tex_path, final_pdf_path):
        print(f"Skipping {final_pdf_path}: PDF up to date with {tex_path}")
        return True

    tool = config["LatexExecutable"]

    output_tex_path = "draft.tex"
    output_pdf_path = "draft.pdf"
    if os.path.exists(output_pdf_path):
        os.remove(output_pdf_path)

    # Only prepend macOS TeX path if it exists; do not pollute PATH otherwise.
    texbin = "/Library/TeX/texbin"
    if os.path.isdir(texbin) and texbin not in os.environ.get("PATH", ""):
        os.environ["PATH"] = texbin + os.pathsep + os.environ.get("PATH", "")

    with open(output_tex_path, "w") as out:
        out.write(_read("../Support/minibookheader.tex"))
        out.write(f"\\graphicspath{{{{{chap_dir}/}}}}\n")
        out.write(f"\\input{{{chap_dir}/{chapter_file}}}\n")
        out.write(_read("../Support/draftmsg.tex"))
        out.write(_read("../Support/bookfooter.tex"))

    cmd = [tool, "-halt-on-error", "-shell-escape", output_tex_path]
    subprocess.run(cmd)
    if draft:
        # Second pass for cross-references.
        subprocess.run(cmd)

    if os.path.exists(output_pdf_path):
        shutil.move(output_pdf_path, final_pdf_path)
        print(f"{final_pdf_path} built.")
        return True
    print(f"Build of {final_pdf_path} Failed")
    return False


# Not checking "files" attribute
def urls_in_chapter_meta(chap_meta):
    result = []
    for topic in chap_meta.get("covers", []):
        result.extend(topic.get("references", []))
        result.extend(topic.get("videos", []))
    return result
