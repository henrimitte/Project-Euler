from tools import sieve_of_eratosthenes


primes = sieve_of_eratosthenes(1000000)


def is_sum_of_consecutive_primes(n):
    index = start = soma = counter = 0
    possible = True
    while possible:
        soma += primes[index]
        counter += 1
        if soma == n:
            return counter
        elif soma < n:
            index += 1
        elif soma > n:
            soma = 0
            counter = 0
            start += 1
            index = start
        if primes[index] >= n:
            possible = False
    return 0


reps = num = 0
for p in reversed(primes):
    cp = is_sum_of_consecutive_primes(p)
    if cp > reps:
        print(f'Número: {p} Tamanho rep {cp}')
        reps = cp
        num = p

print(
    f'Biggest prime below 1E6 that can be written as a sum of consecutive primes: {num} {reps=}')
