def fib(limit = 1000):
    a, b, s = 1, 2, 2
    while True:
        nxt = a + b
        if nxt % 2 == 0:
            s += nxt
        a = b
        b = nxt
        if a + b > limit:
            break
    return s

print(fib(4000000))
