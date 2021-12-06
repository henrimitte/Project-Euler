def solve():
    from string import ascii_uppercase

    alphanum = dict(zip(ascii_uppercase, range(1, 27)))
    total = 0

    with open('ext_files/p022_names.txt') as arq:
        line = arq.read()
        line = line.replace('"', '')
        names = line.split(',')
        names.sort()

    for i, n in enumerate(names, start=1):
        s = 0
        for letra in n:
            s += alphanum[letra]
        total += (s * i)

    print(total)


if __name__ == '__main__':
    solve()
