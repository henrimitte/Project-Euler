from tools import get_pythagorean_triplet


def solve():
    found = False
    m, n = 2, 1
    while not found:
        triplet = get_pythagorean_triplet(m, n)
        s = sum(triplet)
        if s == 1000:
            print(triplet, s)
            found = True
        elif s > 1000:
            n += 1
            m = n
        m += 1


if __name__ == '__main__':
    solve()
