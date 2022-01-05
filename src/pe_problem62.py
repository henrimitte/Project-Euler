def solve():
    n = 1000
    cubes = {x: sorted(str(x**3)) for x in range(n, 9000)}
    not_found = True
    while not_found:
        checking = cubes[n]
        perms = tuple(filter(lambda v: v == checking, cubes.values()))
        if len(perms) == 5:
            print(n ** 3)
            not_found = False
        n += 1


if __name__ == '__main__':
    solve()
