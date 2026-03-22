import re
mod_dir = "../../Chapters"
vol_count = 36

# script assumes that build workbooks all has been run, st all book aux files exist

for i in range(1, vol_count + 1):
    book_num = str(i).zfill(2)
    path_for_aux = f"./Intermediate/workbook-{book_num}.aux"
    aux_file = open(path_for_aux, "r")
    aux = aux_file.read()
    aux_file.close()

    search_string = r"@abspage@last\{(\d+)\}" # \@abspage@last{63} where 63 is the num of pages
    match = re.search(search_string, aux)
    if match: 
        num1 = int(match.groups()[0])
        print(f"workbook {book_num} -- {num1} pages")
    else:
        print("-1")