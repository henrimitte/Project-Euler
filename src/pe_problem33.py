from tools import greatest_common_divisor


def solve():
    num = den = 1
    for c in range(10, 100):
        for d in range(c + 1, 100):
            a, b = int(str(c)[0]), int(str(d)[-1])
            equal_num = str(c)[-1] == str(d)[0]
            if equal_num and b > 0 and a / b == c / d:
                num *= c
                den *= d

    print(den // greatest_common_divisor(num, den))


if __name__ == '__main__':
    solve()
