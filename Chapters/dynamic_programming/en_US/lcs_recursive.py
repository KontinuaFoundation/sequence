calls = 0

def lcs_length(a, b):
    global calls
    calls += 1
    if a == "" or b == "":
        return 0
    if a[-1] == b[-1]:
        return lcs_length(a[:-1], b[:-1]) + 1
    return max(lcs_length(a[:-1], b), lcs_length(a, b[:-1]))

print(lcs_length("SHOE", "HOSE"), "after", calls, "calls")
calls = 0
print(lcs_length("DYNAMICPROG", "PROGRAMMING"), "after", calls, "calls")
