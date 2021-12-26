def solve():
    mults = [[f'{x:>03}' for x in range(p, 1000, p)]
             for p in (2, 3, 5, 7, 11, 13, 17)]
    mults = [[m for m in mults[p] if len(set(m)) == 3] for p in range(7)]

    chains = mults[-1].copy()
    for i in range(5, -1, -1):
        new_chains = []
        for n in chains:
            possible_chains = [(x[0] + n) for x in mults[i]
                               if x.endswith(n[:2])
                               and len(set(n).union(x)) == len(n) + 1]

            new_chains.extend(possible_chains)
        chains = new_chains[:]

    for i, c in enumerate(chains):
        last_n = set('0123456789').difference(set(c)).pop()
        chains[i] = last_n + chains[i]

    print(sum(map(int, chains)))


if __name__ == '__main__':
    solve()
