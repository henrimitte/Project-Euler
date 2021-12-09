from tools import factorial


def solve():
    fa = tuple(factorial(x) for x in range(10))
    s = 0
    for c in range(3, 100000):
        if c == sum(fa[int(x)] for x in str(c)):
            s += c

    print(s)


if __name__ == '__main__':
    solve()
