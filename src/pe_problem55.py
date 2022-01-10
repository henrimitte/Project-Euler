from tools import reverse_int, is_palindrome


def _is_lychrel_num(n: int) -> bool:
    its = 0
    while its < 50:
        n += reverse_int(n)
        if is_palindrome(n):
            return False
        its += 1
    return True


def solve():
    lychrel_nums = 0
    for c in range(10000):
        if _is_lychrel_num(c):
            lychrel_nums += 1
    print(lychrel_nums)


if __name__ == '__main__':
    solve()
