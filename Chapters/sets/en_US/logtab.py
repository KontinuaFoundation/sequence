import itertools

a = False
b = False

c = a or not b
print(f"a={a}, b={b}, a or not b = {c}")                                                                      

all_combos = itertools.product([False, True], repeat=2)
for (a, b) in all_combos:
    result = a or not b
    print(f"a={a}, b={b}: a or not b = {result}")                                                                        

all_combos = itertools.product([False, True], repeat=3)
for (a, b, c) in all_combos:
    result = a and not(b and c)
    print(f"a={a}, b={b}, c={c}: a and not (b and c) = {result}")     