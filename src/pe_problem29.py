def solve():
    s = set((c ** d for c in range(2, 101) for d in range(2, 101)))
    print(len(s))


if __name__ == '__main__':
    solve()
