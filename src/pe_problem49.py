from tools import sieve_of_eratosthenes


def _are_permutations(n: int, others: tuple) -> bool:
    to_compare = sorted(str(n))
    return all(sorted(str(x)) == to_compare for x in others)


def solve():
    primes = [p for p in sieve_of_eratosthenes(10000) if p > 1487]
    not_found = True
    i = 0
    while not_found:
        p = primes[i]
        p2, p3 = p + 3330, p + 6660
        if _are_permutations(p, (p2, p3))\
                and all(n in primes for n in (p2, p3)):
            print(str(p) + str(p2) + str(p3))
            not_found = False
        i += 1


if __name__ == '__main__':
    solve()
