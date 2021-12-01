from TOOLS import factorial

div = 2, 3, 5, 7, 11, 13, 17


def all_div(n):
    n = str(n)
    for c in range(7):
        if int(n[c + 1:c + 4]) % div[c] != 0:
            return False
    return True


def get_nth_ordered_permutation(nth, size=10):
    nums = list('0123456789')
    nth -= 1
    s = ''
    for c in range(size - 1, -1, -1):
        f = factorial(c)
        d, m = divmod(nth, f)
        s += nums.pop(int(d))
        nth = m

    return int(s)


s = 0
if __name__ == '__main__':
    l = (get_nth_ordered_permutation(c) for c in range(1, factorial(10)))
    for n in l:
        if (all_div(n)):
            s += n
            print(n)

    print(f'final: {s}')
