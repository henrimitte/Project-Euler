from tools import sieve_of_eratosthenes as sieve

limit_of_primes = 65500
print(f'Generating all prime numbers < {limit_of_primes}')
primes = sieve.sieve_of_eratosthenes(limit_of_primes)
print('Succesfully generated prime numbers!')


def generate_triangule_numbers(n_limit):
    return int(0.5 * n_limit * (n_limit + 1))


def decompose(num):
    div_exp = []
    index = 0
    while True:
        p = primes[index]
        if num < 2:
            break
        if num % p == 0:
            div_exp.append(p)
            num //= p
        else:
            index += 1

    return div_exp


def number_of_divisors(list_of_prime_factors):
    times = {}
    for c in list_of_prime_factors:
        if c in times.keys():
            continue
        times[c] = list_of_prime_factors.count(c)
    product = 1
    for v in times.values():
        v += 1
        product *= v
    return int(product)


cont = 2
while True:
    tri_num = generate_triangule_numbers(cont)
    result = number_of_divisors(decompose(tri_num))
    if result > 500:
        print(f'Resultado: {tri_num}')
        break
    else:
        cont += 1
