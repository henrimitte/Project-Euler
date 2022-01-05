from math import log10


def solve():
    with open('ext_files/p099_base_exp.txt', 'r') as file:
        content = file.read().split('\n')
        base_exp = [tuple(map(int, line.split(','))) for line in content]

    index = biggest = 0
    for line_index, line in enumerate(base_exp, start=1):
        calc = line[1] * log10(line[0])
        if calc > biggest:
            biggest = calc
            index = line_index

    print(index)


if __name__ == '__main__':
    solve()
