from tools import sieve_of_eratosthenes, is_one_to_n_pandigital


def solve():
    primes = [str(p) for p in sieve_of_eratosthenes(
        10000000) if len(set(str(p))) == len(str(p))]
    primes.reverse()
    not_found = True
    i = 0
    while not_found:
        if is_one_to_n_pandigital(primes[i], len(primes[i])):
            not_found = False
        else:
            i += 1
    print(primes[i])


if __name__ == '__main__':
    solve()
