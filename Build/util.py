import os
import re
import json
import shutil

title_pattern = re.compile("chapter\{([^\}]+)\}")
# chapter_pattern = re.compile("chapter\}\{\\\\numberline \{([^\}]+)\}[^\}]+\{([0-9]+)\}")
chapter_pattern = re.compile("chapter\}\{\\\\numberline \{([^\}]+)\}[^\}]+\}\{([0-9]+)\}")

def chapter_toc(bookstr):
    toc = {}
    chapter_path = f"Intermediate/workbook-{bookstr}.toc"
    with open(chapter_path) as f:
        for i, line in enumerate(open(chapter_path)):
            for match in re.finditer(chapter_pattern, line):
                chapter = match.group(1)
                page = int(match.group(2))
                toc[chapter] = page
    return toc

def dir_for_id(mod_dir, identifier, langlist):
    # FIXME: should search from fav to least fave
    locale_str = langlist[0]
    return os.path.join(mod_dir,identifier,locale_str)

def dir_list_for_book(mod_dir, book_str, langlist):
    # FIXME: should search from fav to least fave
    modlist_filename = f"book_{book_str}.txt"
    modlist_path = os.path.join(mod_dir, modlist_filename)
    if not os.path.exists(modlist_path):
        print(f"Error: Chapter file {modlist_path} doesn't exist")
        return []
    modlist = open(modlist_path, "r")
    chapters = modlist.readlines()
    modlist.close()

    result_paths = []
    result_ids = []
    for chapter in chapters:
        trimmed_chapter = chapter.strip()
        if trimmed_chapter[0] != "#" and len(trimmed_chapter) > 0:
            print(f"Processing {trimmed_chapter}")
            result_ids.append(trimmed_chapter)
            fullpath = dir_for_id(mod_dir,trimmed_chapter,langlist)
            result_paths.append(fullpath)
        else:
            print(f"Skipping {trimmed_chapter}")
    return (result_ids, result_paths)

def title_for_dir(dir):
    fullpath = os.path.join(dir, "student.tex")
    for i, line in enumerate(open(fullpath)):
        for match in re.finditer(title_pattern, line):
            return match.group(1)
    return "UNKNOWN"

def metadata_for_dir(dir):
    rpath = os.path.join(dir, "digital_resources.json")
    if not os.path.exists(rpath):
        print(f"Error: Resources file file {rpath} doesn't exist")
        result = {}
    else:
        with open(rpath, 'r') as f:
            data = f.read().strip()
        if len(data) < 2:
            result = {}
        else:
            result = json.loads(data)
    title = title_for_dir(dir)
    result["title"] = title
    return result

def gather_data(mod_dir, book_str, config):
    (ids, dirs) = dir_list_for_book(mod_dir, book_str, config["Languages"])
    metadatas = []
    topics = {}
    for (i, dir) in enumerate(dirs):
        md = metadata_for_dir(dir)
        # Get the title from the tex file
        title = title_for_dir(dir)

        # Fill in some useful info
        md["book"] = book_str
        md["id"] = ids[i]
        md["title"] = title
        md["chap_num"] = i + 1

        # Make URLs for the files
        if "files" in md:
            filelist = md["files"]
            for j in range(len(filelist)):
                filename = filelist[j]["path"]
                filelist[j]["link"] = f"https://github.com/TheKontinua/sequence/raw/master/Chapters/{ids[i]}/en_US/{filename}"
        # Add it to the array
        metadatas.append(md)

        # Also put the data in the topics dictionary
        if "covers" in md:
            for c in md["covers"]:
                cd = c.copy()
                cd["book"] = book_str
                cd["chap_title"] = title
                cd["chap_num"] = i + 1
                cd["chap_id"] = ids[i]
                topics[cd["id"]] = cd

    return (metadatas, topics)

def build_chapter(chapter_file, chap_dir, config, final_pdf_path, draft=True):
    locale_list = config["Languages"]
    paper_size = config["Paper"]
    tool = config["LatexExecutable"]

    output_tex_path = "draft.tex"
    output_pdf_path = "draft.pdf"
    if os.path.exists(output_pdf_path):
        os.remove(output_pdf_path)
    output_tex = open(output_tex_path, "w")

    # Write the header
    header_file = open("../Support/minibookheader.tex", "r")
    header = header_file.read()
    header_file.close()
    output_tex.write(header)

    gpath_string = "\\graphicspath{{{{{}/}}}}\n".format(chap_dir)
    output_tex.write(gpath_string)


    # Include file
    full_path = os.path.join(chap_dir, chapter_file)
    include_string = "\\input{{{}}}\n".format(full_path)
    output_tex.write(include_string)

    # Draft message
    with open("../Support/draftmsg.tex","r") as draft_file:
        draftmsg = draft_file.read()
        output_tex.write(draftmsg)

    # Write the footer
    footer_file = open("../Support/bookfooter.tex", "r")
    footer = footer_file.read()
    footer_file.close()
    output_tex.write(footer)
    output_tex.close()
    os.system(f"{tool} -halt-on-error {output_tex_path}")

    if not draft:
        # Run it a second time to make cross-references
        os.system(f"{tool} -halt-on-error {output_tex_path}")
    if os.path.exists(output_pdf_path):
        shutil.move(output_pdf_path, final_pdf_path)
        print(f"{final_pdf_path} built.")
        return True
    else:
        print(f"Build of {final_pdf_path} Failed")
        return False

# Not checking "files" attribute
def urls_in_chapter_meta(chap_meta):
    result = []
    if 'covers' in chap_meta:
        cover_list = chap_meta['covers']
        for topic in cover_list:
            if 'references' in topic:
                reference_list = topic['references']
                for reference in reference_list:
                    result.append(reference)
            if 'videos' in topic:
                video_list = topic['videos']
                for video in video_list:
                    result.append(video)
    return result
