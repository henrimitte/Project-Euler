from tools import sum_divisible_by


def solve():
    target = 999
    div_by_tree = sum_divisible_by(3, target)
    div_by_five = sum_divisible_by(5, target)
    div_by_fifteen = sum_divisible_by(3 * 5, target)
    ans = div_by_tree + div_by_five - div_by_fifteen
    print(ans)


if __name__ == '__main__':
    solve()
