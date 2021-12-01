'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
'''
def _isPrime(num):
    for c in range(2, num - 1,):
        if num % c == 0:
            return False
    return True

primes = []
c = 1
n = 2
while len(primes) < 10001:
    if _isPrime(n):
        primes.append(n)
        c += 1
    n += 1

print(primes[-1])
