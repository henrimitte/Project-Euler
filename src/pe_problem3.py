from tools import sieve_of_eratosthenes


def solve():
    i = 0
    n = 600851475143
    primes = sieve_of_eratosthenes(7100)
    while n > 1:
        if n % primes[i] == 0:
            n //= primes[i]
        else:
            i += 1
    print(primes[i])


if __name__ == '__main__':
    solve()
