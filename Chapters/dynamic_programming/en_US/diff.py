from lcs import lcs_table

def diff(old, new):
    table = lcs_table(old, new)
    i, j = len(old), len(new)
    lines = []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and old[i - 1] == new[j - 1]:
            lines.append("  " + old[i - 1])     # in both: unchanged
            i -= 1
            j -= 1
        elif j > 0 and (i == 0 or table[i][j - 1] >= table[i - 1][j]):
            lines.append("+ " + new[j - 1])     # only in new: added
            j -= 1
        else:
            lines.append("- " + old[i - 1])     # only in old: deleted
            i -= 1
    lines.reverse()
    return lines

monday = ["Buy poster board", "Finish lab report", "Email Ms. Rivera",
          "Practice trumpet", "Return library book"]
tuesday = ["Buy poster board", "Finish lab report", "Practice trumpet",
           "Study for chem quiz", "Return library book"]

for line in diff(monday, tuesday):
    print(line)
