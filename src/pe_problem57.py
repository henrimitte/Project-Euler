def solve():
    total = 1
    num, den = 1393, 985
    for c in range(9, 1001):
        num += (den * 2)
        den = num - den
        if len(str(num)) > len(str(den)):
            total += 1

    print(total)


if __name__ == '__main__':
    solve()
