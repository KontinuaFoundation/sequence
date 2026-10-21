# Number Theory and Cryptography: Summary

## What the chapter covers
Builds the number theory behind RSA:
- divisibility and the division algorithm;
- primes (the Fundamental Theorem of Arithmetic, Euclid's proof that there are infinitely many, trial division up to √n, and the Sieve of Eratosthenes);
- the gcd and the Euclidean algorithm, with Bézout coefficients;
- modular arithmetic (congruence, reducing as you go, inverses, fast powers by repeated squaring);
- Fermat's Little Theorem, with a proof and the Fermat primality test.
It ends with RSA: key generation, encryption and decryption, why decryption works, and why it is secure.

## Key ideas
- a | b means b = ak; a = qb + r with 0 ≤ r < b (Python's // and %).
- Every integer > 1 factors into primes in exactly one way, and there are infinitely many primes.
- gcd(a, b) = gcd(b, a mod b); running it backward gives ax + by = gcd(a, b).
- a has an inverse mod n exactly when gcd(a, n) = 1.
- Fermat: if p is prime and p ∤ a, then a^{p−1} ≡ 1 (mod p).
- RSA: n = pq, ed ≡ 1 mod (p−1)(q−1); c = m^e mod n, m = c^d mod n. Security rests on how hard it is to factor n.

## Changes in this pass
- New chapter, placed at the end of volume 5, after inverses_transformations.
- Why volume 5: its prerequisites are proofs (volume 3: direct proof and contradiction) and Python's %, //, while loops, and functions (volumes 3–4). RSA decryption is presented as the inverse of encryption, building on the previous chapter.
- Includes 3 code listings (sieve.py, gcd.py, rsa.py, also saved as digital resources), with their real output; a mod-12 clock figure; 4 theorems with proofs; and 9 exercises with answers (factoring, proofs, Euclid by hand, modular inverses, Fermat, pseudoprimes and Carmichael numbers, RSA by hand, why e must be coprime to φ, breaking a small key).
- All values verified in Python (for example, d = 2753 and c = 2790 for p = 61, q = 53; 2^340 ≡ 1 mod 341; 78,498 primes below one million; 3^2026 has 967 digits).
