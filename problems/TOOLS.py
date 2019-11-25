from math import sqrt


def sieve_of_eratosthenes(limit = 100):
    '''Return a list with all prime numbers below the limit.'''
    limit = abs(limit)
    if limit < 2:
        return []

    max_num_to_check = int(sqrt(limit)) + 1
    all_numbers = [x for x in range(3, limit, 2)] # Get only odd numbers
    index = 0
    while True:
        number_being_checked = all_numbers[index]
        all_numbers = [x for x in all_numbers
                       if x == number_being_checked
                       or x % number_being_checked != 0]
        index += 1
        next_prime = all_numbers[index]
        if next_prime > max_num_to_check:
            all_numbers.insert(0, 2) # Insert 2 at index 0, as 2 is the first prime
            return all_numbers


def factorial(num):
    num = abs(num)
    if num is (0 or 1):
        return 1
    return num * factorial(num - 1)


def fib(f1 = 0, f2 = 1, limit = 100):
    '''Return a list with the fibonacci sequence to the nth (limit) index'''
    index = 2
    fib_seq = [f1, f2]
    while True:
        index += 1
        next_num = f1 + f2
        fib_seq.append(next_num)
        f1, f2 = f2, next_num
        if index is limit:
            return fib_seq

def simple_combination(n, p):
    fact_n = factorial(n)
    fact_p = factorial(p)
    fact_np = factorial(n - p)
    return fact_n / (fact_p * fact_np)
