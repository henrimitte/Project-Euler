from TOOLS import sieve_of_eratosthenes

primes = sieve_of_eratosthenes(500000)


def factorize(n):
    factors = []
    i = 0
    while n > 1:
        checking = primes[i]
        if n % checking == 0:
            factors.append(checking)
            n //= checking
        else:
            i += 1
    return factors


for c in range(100001, 1000000, 2):
    factors = [set(factorize(c + i)) for i in range(0, 4)]
    if all((len(f) == 4 for f in factors)):
        print(c, factors)
        break
