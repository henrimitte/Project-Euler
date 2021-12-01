from tools import sieve_of_eratosthenes as sieve

limit = 10000
primes = sieve(limit)
odd_composites = list(filter(lambda x: x not in primes, range(9, limit, 2)))
squares = [x*x for x in range(1, int(limit**0.5) + 1)]


def _can_be_prime_and_twice_square(n: int):
    while 1:
        for p in primes:
            for square in squares:
                o = p + 2 * square
                if (o == n):
                    return True
        if (o > n):
            return False


def solve():
    for n in odd_composites:
        if not _can_be_prime_and_twice_square(n):
            print(n)
    print('done')


if __name__ == '__main__':
    solve()
