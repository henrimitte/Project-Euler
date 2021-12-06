from tools import sieve_of_eratosthenes, sum_of_ints


def solve():
    n = 3
    Dn = 2
    cnt = 0
    n1 = Dn1 = exponent = 0
    primes = sieve_of_eratosthenes(1000)

    while cnt <= 500:
        n += 1
        n1 = n
        if n1 % 2 == 0:
            n1 //= 2
        Dn1 = 1
        for p in primes:
            if p ** 2 > n1:
                Dn1 *= 2
                break

            exponent = 1
            while n1 % p == 0:
                exponent += 1
                n1 //= p
            if exponent > 1:
                Dn1 *= exponent
            if n1 == 1:
                break
        cnt = Dn * Dn1
        Dn = Dn1
    print(sum_of_ints(n))


if __name__ == '__main__':
    solve()
