from tools import is_palindrome


def solve():
    largest = 0
    a = 999
    while a >= 100:
        b = a
        while b >= a:
            mult = a * b
            if mult <= largest:
                break

            if is_palindrome(mult):
                largest = mult

            b -= 1
        a -= 1

    print(largest)


if __name__ == '__main__':
    solve()
