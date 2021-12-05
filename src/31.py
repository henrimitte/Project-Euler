def _count(S, m, n):
    if n == 0:
        return 1

    if n < 0:
        return 0

    if m <= 0 and n >= 1:
        return 0

    return _count(S, m - 1, n) + _count(S, m, n-S[m-1])


def solve():
    am = 200
    coins = [5, 10, 20, 50, 100, 200]
    m = len(coins)
    print(_count(coins, m, am))


if __name__ == '__main__':
    solve()
