from tools import max_path_sum


def solve():
    triangle = []
    with open('ext_files/p067_triangle.txt') as arq:
        for row in arq.readlines():
            triangle.append([int(x) for x in row.split(' ')])

    print(max_path_sum(triangle))


if __name__ == '__main__':
    solve()
