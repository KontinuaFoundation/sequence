from math import gcd

# Key generation
p, q = 61, 53
n = p * q                    # public
phi = (p - 1) * (q - 1)      # secret
e = 17                       # public
assert gcd(e, phi) == 1
d = pow(e, -1, phi)          # secret: the inverse of e mod phi
print("n =", n, " phi =", phi, " d =", d)

# Encrypt and decrypt a message
m = 65
c = pow(m, e, n)             # anyone can do this with (n, e)
print("ciphertext:", c)
print("decrypted:", pow(c, d, n))   # only the key owner knows d
