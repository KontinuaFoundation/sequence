import math

z = 1j * math.pi          # the exponent i*pi
total = 0
for n in range(12):
    total += z**n / math.factorial(n)
    print(n, round(total.real, 4), round(total.imag, 4))
