from tools import get_nth_pentagonal


def _is_pentagonal(n: int) -> bool:
    e = ((24 * n + 1) ** 0.5 + 1) / 6
    return e == int(e)


def solve():
    pentagonals = [get_nth_pentagonal(x) for x in range(1, 3001)]
    not_found = True
    i = 0
    length = len(pentagonals)
    while not_found:
        j = i + 1
        p = pentagonals[i]
        dif_not_found = True
        while j < length and dif_not_found:
            q = pentagonals[j]
            s, d = p + q, abs(q - p)
            if _is_pentagonal(s) and _is_pentagonal(d):
                dif_not_found = not_found = False
            j += 1
        i += 1
    print(d)


if __name__ == '__main__':
    solve()
