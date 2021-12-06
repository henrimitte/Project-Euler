def solve():
    s = sum((x ** x for x in range(1, 1001)))
    print(str(s)[-10:])


if __name__ == '__main__':
    solve()
