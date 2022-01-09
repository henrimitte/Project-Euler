def _leap_year(n: int) -> bool:
    return n % 4 == 0 and (n % 100 != 0 or n % 400 == 0)


def solve():
    months = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    first = 365 % 7 + 1
    sundays = 0
    for year in range(1901, 2001):
        months[1] = 29 if _leap_year(year) else 28
        for d in months:
            if first == 0:
                sundays += 1
            first = (first + d) % 7

    print(sundays)


if __name__ == '__main__':
    solve()
