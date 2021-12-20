from tools import sieve_of_eratosthenes


def _get_num_rotations(n: int) -> list:
    rotations = len(str(n)) - 1
    rotated = set()
    exp = 10 ** rotations
    for _ in range(rotations):
        d, m = divmod(n, 10)
        n = d + (m * exp)
        rotated.add(n)
    return rotated


def solve():
    primes = sieve_of_eratosthenes(1000000)[5:]
    limit = min(_get_num_rotations(primes[-1]))
    not_done = True
    circular_primes = 5
    while not_done:
        checking = primes.pop(0)
        rotations = _get_num_rotations(checking)
        if all(n in primes for n in rotations):
            circular_primes += len(rotations) + 1
            for p in rotations:
                primes.remove(p)
        if checking > limit:
            not_done = False

    print(circular_primes)


if __name__ == '__main__':
    solve()
