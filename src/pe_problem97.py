def solve():
    prime = (28433 * 2**7830457) + 1) % 10000000000
        last_ten_digits=str(prime)[-10:]
        print(last_ten_digits)


if __name__ == '__main__':
    solve()
