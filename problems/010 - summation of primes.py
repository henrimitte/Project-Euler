def _isPrime(num):
    for c in range(2, num - 1,):
        if num % c == 0:
            return False
    return True

soma = 0
for c in range(2, 2000000):
    if c % 1000 == 0:
        print(c)
    if _isPrime(c):
        soma += c

print(soma)
