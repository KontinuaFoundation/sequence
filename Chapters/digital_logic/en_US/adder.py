nand_count = 0

def nand(a, b):
    global nand_count
    nand_count += 1
    return 0 if (a == 1 and b == 1) else 1

# Every other gate is built from NAND
def not_(a):
    return nand(a, a)

def and_(a, b):
    return not_(nand(a, b))

def or_(a, b):
    return nand(not_(a), not_(b))

def xor(a, b):
    n = nand(a, b)
    return nand(nand(a, n), nand(b, n))

def full_adder(a, b, carry_in):
    s = xor(a, b)
    total = xor(s, carry_in)
    carry_out = or_(and_(a, b), and_(s, carry_in))
    return total, carry_out

def add(a_bits, b_bits):
    # Bits are listed from least significant to most significant
    carry = 0
    result = []
    for a, b in zip(a_bits, b_bits):
        total, carry = full_adder(a, b, carry)
        result.append(total)
    result.append(carry)
    return result

def to_bits(n, width):
    return [(n >> i) & 1 for i in range(width)]

def to_int(bits):
    return sum(bit << i for i, bit in enumerate(bits))

print("6 + 7 =", to_int(add(to_bits(6, 4), to_bits(7, 4))))

# Test every pair of 4-bit numbers
errors = 0
for x in range(16):
    for y in range(16):
        if to_int(add(to_bits(x, 4), to_bits(y, 4))) != x + y:
            errors += 1
print("pairs tested: 256, errors:", errors)

nand_count = 0
add(to_bits(6, 4), to_bits(7, 4))
print("NAND gates used for one 4-bit addition:", nand_count)
