def sieve_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for current in range(2, int(limit ** 0.5) + 1):
        if sieve[current]:
            for multiple in range(current * current, limit + 1, current):
                sieve[multiple] = False

    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes

# Example usage:
limit = 20
print(sieve_eratosthenes(limit))