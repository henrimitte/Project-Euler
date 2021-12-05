from tools import sieve_of_eratosthenes


def solve():
    limit = 2000000
    primes = sieve_of_eratosthenes(limit)
    print(sum(primes))


if __name__ == '__main__':
    solve()
