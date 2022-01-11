from tools import get_nth_s_gonal, is_s_gonal


def solve():
    pentagonals = [get_nth_s_gonal(5, x) for x in range(1, 3001)]
    not_found = True
    i = 0
    length = len(pentagonals)
    while not_found:
        j = i + 1
        p = pentagonals[i]
        dif_not_found = True
        while j < length and dif_not_found:
            q = pentagonals[j]
            s, d = p + q, abs(q - p)
            if is_s_gonal(5, s) and is_s_gonal(5, d):
                dif_not_found = not_found = False
            j += 1
        i += 1
    print(d)


if __name__ == '__main__':
    solve()
