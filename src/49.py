from TOOLS import sieve_of_eratosthenes

primes = sieve_of_eratosthenes(10000)
primes = [p for p in primes if p > 1000]


def get_permutations(n, l):
    to_find = sorted(str(n))
    return [n for n in l if sorted(str(n)) == to_find]


def get_difs(n, l):
    return [abs(p - n) for p in l if p != n]


while primes:
    perms = get_permutations(primes[0], primes)
    for p in perms:
        primes.remove(p)
    if len(perms) > 2:
        all_difs = [get_difs(p, perms) for p in perms]
        # print(all_difs):
        for ld in all_difs:
            for n in ld:
                if n > 1000 and sum((1 if n in l else 0 for l in all_difs)) == 3:
                    print(perms, n)
