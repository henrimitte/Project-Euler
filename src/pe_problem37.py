from tools import sieve_of_eratosthenes


def _prime_filter(n: int) -> bool:
    return (n % 10 in (1, 3, 5, 7, 9)) \
        and (n // 10 ** (len(str(n)) - 1) in (1, 2, 3, 5, 7, 9)) \
        and all(int(x) % 2 != 0 for x in str(n)[1:])


def _left_to_right(n: int) -> bool:
    return all((n % (10 ** c)) in primes for c in range(1, len(str(n))))


def _right_to_left(n: int) -> bool:
    return all((n // (10 ** c)) in primes for c in range(1, len(str(n))))


primes = [2, 3, 5, 7] + \
    list(filter(_prime_filter, sieve_of_eratosthenes(1000000)[5:]))


def solve():
    s, found, index = 0, 0, 4
    while found < 11:
        prime = primes[index]
        if _left_to_right(prime) and _right_to_left(prime):
            found += 1
            s += prime
        index += 1

    print(s)


if __name__ == '__main__':
    solve()
