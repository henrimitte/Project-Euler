from itertools import dropwhile
from tools import sieve_of_eratosthenes


primes = sieve_of_eratosthenes(1000000)
to_check = list(dropwhile(lambda x: x < 997000, primes))


def _consecutive_primes(n: int) -> int:
    index = start = soma = counter = 0
    limit = (n + 3) // 2
    while primes[index] < limit:
        soma += primes[index]
        counter += 1
        if soma == n:
            return counter
        elif soma < n:
            index += 1
        elif soma > n:
            soma = 0
            counter = 0
            start += 1
            index = start
    return 0


def solve():
    reps = num = 0
    for p in to_check:
        cp = _consecutive_primes(p)
        if cp > reps:
            reps = cp
            num = p
    print(num)


if __name__ == '__main__':
    solve()
