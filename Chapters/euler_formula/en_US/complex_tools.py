import cmath, math

print(cmath.exp(1j * math.pi))         # e^(i pi)
print(cmath.polar(1 + 1j))             # (r, theta) for 1 + i
print(cmath.rect(2, math.pi / 3))      # 2 e^(i pi/3) back to a + bi
print((1 + 1j) ** 10)                  # De Moivre says 32i
