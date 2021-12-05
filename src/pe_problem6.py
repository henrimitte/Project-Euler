from tools import sum_of_squares, sum_of_ints


def solve():
    sum_squares = sum_of_squares(100)
    square_of_sum = sum_of_ints(100) ** 2
    print(square_of_sum - sum_squares)


if __name__ == '__main__':
    solve()
