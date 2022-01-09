def _is_abundant(n: int) -> bool:
    limit = n // 2 + 1
    s = 1
    for c in range(2, limit):
        if n % c == 0:
            s += c
    return s > n


def solve():
    limit = 28124
    can_be_written = [False for _ in range(limit)]
    abundants = list(filter(_is_abundant, range(12, limit)))
    i = 0
    while abundants[i] < limit // 2 + 1:
        current = abundants[i]
        ni = i
        while (current + abundants[ni]) < limit:
            can_be_written[current + abundants[ni]] = True
            ni += 1
        i += 1

    print(sum(x for x in range(limit) if not can_be_written[x]))


if __name__ == '__main__':
    solve()
