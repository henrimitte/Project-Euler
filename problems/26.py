from decimal import Decimal, getcontext


def split_by_interval(s: str, n: int) -> list:
    return [s[c:c + n] for c in range(0, len(s) // n * n, n)]


def get_repetition_size(s: str) -> int:
    for c in range(1, len(s) // 2):
        splitted = split_by_interval(s, c)
        all_equal = (splitted[0] == x for x in splitted[1:])
        if all(all_equal):
            return c
    return 0


biggest = the_num = 1
getcontext().prec = 2000
for c in range(3, 1000, 2):
    div = str(Decimal(1) / Decimal(c))[2:]
    for d in range(0, len(div) // 2, biggest):
        rep_size = get_repetition_size(div[d:])
        if rep_size > biggest:
            the_num = c
            biggest = rep_size
            print(f'Novo recorde: {c}, {rep_size}')
            break

print(f'O número: {the_num}\nTamanho: {biggest}')
