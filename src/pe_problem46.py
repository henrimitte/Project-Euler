from tools import sieve_of_eratosthenes

_limit = 10000
_primes = sieve_of_eratosthenes(_limit)
_odd_composites = [x for x in range(9, _limit, 2) if x not in _primes]
_squares = [x*x*2 for x in range(1, int(_limit**0.5) + 1)]


def _can_be_prime_and_twice_square(n: int) -> bool:
    pi = 0
    while _primes[pi] < n:
        si = 0
        while _squares[si] < n:
            if ((_primes[pi] + _squares[si]) == n):
                return True
            si += 1
        pi += 1
    return False


def solve():
    not_found = True
    i = 0
    while not_found:
        if not _can_be_prime_and_twice_square(_odd_composites[i]):
            print(_odd_composites[i])
            not_found = False
        i += 1


if __name__ == '__main__':
    solve()
