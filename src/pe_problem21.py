def _sum_of_proper_divisors(n: int) -> int:
    divisors = 1
    for c in range(2, (n // 2) + 1):
        if n % c == 0:
            divisors += c
    return divisors


def solve():
    limit = 10000
    s_divs = tuple(_sum_of_proper_divisors(x) for x in range(limit))
    s = 0
    for c in range(limit):
        if (s_divs[c] < 10000) and (c == s_divs[s_divs[c]]) and (c != s_divs[c]):
            s += c

    print(s)


if __name__ == '__main__':
    solve()
