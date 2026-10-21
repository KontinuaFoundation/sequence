def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(1071, 462))
print(gcd(252, 198))
