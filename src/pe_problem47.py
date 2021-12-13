from tools import sieve_of_eratosthenes

_primes = sieve_of_eratosthenes(150000)


def _dist_factors(n: int) -> int:
    distinct_factors = i = 0
    while n > 1:
        if n % _primes[i] == 0:
            distinct_factors += 1
            while n % _primes[i] == 0:
                n //= _primes[i]
        i += 1

    return distinct_factors


def solve():
    last = 100000
    not_found = True
    a, b, c, d = (_dist_factors(last + x) for x in range(4))
    while not_found:
        if all(x == 4 for x in (a, b, c, d)):
            not_found = False
        else:
            last += 1
            a, b, c, d = b, c, d, _dist_factors(last + 3)

    print(last)


if __name__ == '__main__':
    solve()
