values = {1: 1}


def _count_chain(n: int):
    if n in values.keys():
        return values[n]

    if n % 2 == 0:
        values[n] = 1 + _count_chain(n // 2)
    else:
        values[n] = 2 + _count_chain((3 * n + 1) // 2)

    return values[n]


def solve():
    start = 1000000 // 2
    longest_chain = ans = 0

    for c in range(start, 1000000):
        chain = _count_chain(c)
        if chain > longest_chain:
            longest_chain = chain
            ans = c

    print(ans)


if __name__ == '__main__':
    solve()
