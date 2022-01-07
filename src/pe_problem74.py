from tools import factorial


def solve():
    fa = tuple(factorial(x) for x in range(10))

    def _sum_factorial_of_digits(n: int) -> int:
        s = 0
        while n > 0:
            s += fa[n % 10]
            n //= 10
        return s

    limit = 1000000
    loops = [0 for x in range(limit)]
    for i in range(limit):
        if not loops[i]:
            loop_not_found = True
            chain = [i]
            n = i
            while loop_not_found:
                n = _sum_factorial_of_digits(n)
                if n in chain:
                    loop_not_found = False
                else:
                    chain.append(n)
            loops[i] = len(chain)

    sixty = sum(filter(lambda v: v == 60, loops)) // 60
    print(sixty)


if __name__ == '__main__':
    solve()
