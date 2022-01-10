def solve():
    s = n = 1
    inc = 2
    while inc < 1002:
        for _ in range(4):
            n += inc
            s += n
        inc += 2
    print(s)


if __name__ == '__main__':
    solve()
