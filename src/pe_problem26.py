from decimal import Decimal, getcontext


def _split_by_interval(s: str, n: int) -> list:
    return [s[c:c + n] for c in range(0, len(s) // n * n, n)]


def _get_repetition_size(s: str) -> int:
    for c in range(1, len(s) // 2):
        splitted = _split_by_interval(s, c)
        all_equal = (splitted[0] == x for x in splitted[1:])
        if all(all_equal):
            return c
    return 0


def solve():
    getcontext().prec = 2000
    i = 999
    found = False
    while not found:
        d = str(Decimal(1) / Decimal(i))[2:]
        rep_size = _get_repetition_size(d)
        if i == (rep_size + 1):
            print(i)
            found = True
        i -= 2


if __name__ == '__main__':
    solve()
