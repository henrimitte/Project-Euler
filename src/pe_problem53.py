from tools import simple_combination


def solve():
    gt_one_million = 0
    for n in range(100, 0, -1):
        for p in range(n, 0, -1):
            if simple_combination(n, p) > 1000000:
                gt_one_million += 1

    print(gt_one_million)


if __name__ == '__main__':
    solve()
