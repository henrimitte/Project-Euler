from tools import is_one_to_n_pandigital


def solve():
    pan = []
    for c in range(10000):
        m = 1
        s = ''
        while len(s) < 9:
            s += str(c * m)
            m += 1
        if is_one_to_n_pandigital(s, 9):
            pan.append(int(s))

    print(max(pan))


if __name__ == '__main__':
    solve()
