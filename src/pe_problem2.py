from tools import get_nth_fibonacci


def solve():
    s, index = 0, 3
    even_fib = get_nth_fibonacci(index)
    while even_fib < 4e6:
        s += even_fib
        even_fib = get_nth_fibonacci(index + 3)
        index += 3
    print(s)


if __name__ == '__main__':
    solve()
