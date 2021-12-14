from tools import get_pythagorean_triplet


def solve():
    found = False
    m, n = 2, 1
    while not found:
        triplet = get_pythagorean_triplet(m, n)
        s = sum(triplet)
        if s == 1000:
            found = True
        elif s > 1000:
            n += 1
            m = n
        m += 1
    print(triplet[0] * triplet[1] * triplet[2])


if __name__ == '__main__':
    solve()
