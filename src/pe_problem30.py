def solve():
    fifth_pwrs = 0
    for c in range(2, 1000000):
        s = sum(int(x) ** 5 for x in str(c))
        if s == c:
            fifth_pwrs += c

    print(fifth_pwrs)


if __name__ == '__main__':
    solve()
