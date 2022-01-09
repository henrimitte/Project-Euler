from tools import sieve_of_eratosthenes


def solve():
    primes = sieve_of_eratosthenes(1000)
    record = product = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            while (n ** 2 + a * n + b) in primes:
                n += 1

            if record < n:
                record = n
                product = a * b

    print(product)


if __name__ == '__main__':
    solve()
