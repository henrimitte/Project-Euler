def solve():
    limit = 1000001
    st = ''
    c = s = start = 1
    while len(st) < limit:
        st += str(c)
        c += 1
    while start < limit:
        s *= int(st[start - 1])
        start *= 10

    print(s)


if __name__ == '__main__':
    solve()
