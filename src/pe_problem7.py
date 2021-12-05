from tools import sieve_of_eratosthenes


def solve():
    primes = sieve_of_eratosthenes(150000)
    print(primes[10001])


if __name__ == '__main__':
    solve()
