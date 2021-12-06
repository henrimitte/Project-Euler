from tools import factorial


def solve():
    print(sum([int(x) for x in str(factorial(100))]))


if __name__ == '__main__':
    solve()
