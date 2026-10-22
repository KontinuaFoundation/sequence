def lcs_table(a, b):
    # table[i][j] = length of the LCS of a[:i] and b[:j]
    table = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table

def lcs(a, b):
    table = lcs_table(a, b)
    # Walk back from the bottom-right corner to recover the letters
    i, j = len(a), len(b)
    letters = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            letters.append(a[i - 1])
            i -= 1
            j -= 1
        elif table[i - 1][j] >= table[i][j - 1]:
            i -= 1
        else:
            j -= 1
    letters.reverse()
    return "".join(letters)

if __name__ == "__main__":
    print(lcs("SHOE", "HOSE"))
    print(lcs("STUDENT", "DENTIST"))
    print(lcs("DYNAMICPROG", "PROGRAMMING"))
