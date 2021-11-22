num = den = 1
for c in range(10, 100):
    for d in range(c + 1, 100):
        a, b = int(str(c)[0]), int(str(d)[-1])
        e = str(c)[-1] == str(d)[0]
        if e and b > 0 and a / b == c / d:
            num *= c
            den *= d


def gcd(a, b):
    while True:
        a, b = b, a % b
        if b == 0:
            return a


print(den / gcd(num, den))
