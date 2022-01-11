from tools import get_nth_s_gonal, is_s_gonal


def solve():
    n = 143
    not_found = True
    while not_found:
        n += 1
        h = get_nth_s_gonal(6, n)
        if is_s_gonal(5, h):
            not_found = False
    print(h)


if __name__ == '__main__':
    solve()
