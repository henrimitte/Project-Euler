from math import sqrt

n = 600851475143
sqr = int(sqrt(n))


def _isPrime(num):
    for c in range(2, num - 1,):
        if num % c == 0:
            return False
    return True


for c in range(2, sqr + 1):
    if n % c == 0 and _isPrime(c):
        print(c)
