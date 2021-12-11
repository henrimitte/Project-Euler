def solve():
    _all_nums = '123456789'
    products = set()
    for c in range(2, 50):
        possible = True
        d = 2
        while possible:
            product = c * d
            concat = str(c) + str(d) + str(product)
            if len(concat) > 9:
                possible = False
            if _all_nums == ''.join(sorted(concat)):
                products.add(product)
            d += 1

    print(sum(products))


if __name__ == '__main__':
    solve()
