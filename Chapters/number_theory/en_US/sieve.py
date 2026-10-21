def primes_up_to(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            # cross out every multiple of p, starting at p * p
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
    return [k for k in range(n + 1) if is_prime[k]]

print(primes_up_to(50))
print(len(primes_up_to(1_000_000)))
