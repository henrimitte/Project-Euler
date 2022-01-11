def solve():
    n = 1
    not_found = True
    while not_found:
        n += 1
        s = sorted(str(n))
        if all(sorted(str(n * x)) == s for x in range(2, 7)):
            not_found = False
    print(n)


if __name__ == '__main__':
    solve()
