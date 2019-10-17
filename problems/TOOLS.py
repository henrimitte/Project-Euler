from math import sqrt

def sieve_of_eratosthenes(limit = 10000):
    max_num_to_check = int(sqrt(limit)) + 1
    all_nums = [x for x in range(2, limit)]
    index = 0
    while True:
        number_being_checked = all_nums[index]
        if number_being_checked >= max_num_to_check:
            break
        for n in all_nums[index + 1:]:
            if n % number_being_checked == 0:
                all_nums.remove(n)
        index += 1
    return all_nums

def factorial(num):
    num = abs(num)
    if num is (0 or 1):
        return 1
    return num * factorial(num - 1)


def fib(f1 = 0, f2 = 1, limit = 100):
    index = 2
    next = 0
    fib_seq = [f1, f2]
    while True:
        index += 1
        next = f1 + f2
        fib_seq.append(next)
        f1 = f2
        f2 = next
        if index is limit:
            return fib_seq

def simple_combination(n, p):
    return factorial(n) / (factorial(p) * factorial(n - p))
