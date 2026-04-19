import os
import re

vol_count = 36
search_re = re.compile(r"@abspage@last\{(\d+)\}")

for i in range(1, vol_count + 1):
    book_num = str(i).zfill(2)
    aux_path = f"./Intermediate/workbook-{book_num}.aux"
    if not os.path.exists(aux_path):
        print(f"workbook {book_num} -- missing {aux_path}")
        continue
    with open(aux_path, "r") as f:
        aux = f.read()
    match = search_re.search(aux)
    if match:
        print(f"workbook {book_num} -- {int(match.group(1))} pages")
    else:
        print(f"workbook {book_num} -- -1")
