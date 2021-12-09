
_squares = tuple(x*x for x in range(10))


def _sum_squares_of_digits(n: int) -> int:
    s = 0
    while n > 0:
        s += _squares[n % 10]
        n //= 10
    return s


def solve():
    eighty_nine, limit = 0, 10000000
    map_limit = (len(str(limit))) * 81
    mapped = [0 for _ in range(map_limit)]
    mapped[1], mapped[89] = 1, 89
    for c in range(1, limit):
        n = _sum_squares_of_digits(c)

        if not mapped[n]:
            loop = [n]
            loop_not_found = True
            while loop_not_found:
                next_n = _sum_squares_of_digits(n)

                if mapped[next_n] or next_n == 1 or next_n == 89:
                    for num in loop:
                        mapped[num] = mapped[next_n]
                    loop_not_found = False

                loop.append(next_n)
                n = next_n

        if mapped[n] == 89:
            eighty_nine += 1

    print(eighty_nine)


if __name__ == '__main__':
    solve()
