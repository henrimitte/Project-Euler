def solve():
    total = 0
    for n in range(1, 20):
        for m in range(1, 25):
            if len(str(n ** m)) == m:
                total += 1

    print(total)


if __name__ == '__main__':
    solve()
