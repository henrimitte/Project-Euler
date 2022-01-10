from tools import sum_digits_of_n


def solve():
    s = (sum_digits_of_n(a**b) for a in range(100) for b in range(100))
    print(max(s))


if __name__ == '__main__':
    solve()
