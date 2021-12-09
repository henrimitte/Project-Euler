from tools import reverse_int


def solve():
    s = 0
    for c in range(1, 1000000):
        b = int(bin(c)[2:])
        base2 = b == reverse_int(b)
        base10 = c == reverse_int(c)
        if base2 and base10:
            s += c

    print(s)


if __name__ == '__main__':
    solve()
