import string
from math import sqrt


def is_palindrome(n: int) -> bool:
    '''
    Check if an integer is palindromic.

    :param n: int
    '''
    return n == reverse_int(n)


def reverse_int(n: int) -> int:
    '''
    Reverse the number and return it.

    :param n: int
    '''
    reversed = 0
    while n > 0:
        reversed = 10 * reversed + n % 10
        n //= 10
    return reversed


def get_nth_fibonacci(nth: int) -> int:
    '''
    Return the nth fibonacci number.

    :param nth: int
    '''
    if nth <= 0:
        return 0
    i = nth - 1
    a = d = 1
    b = c = aux1 = aux2 = 0
    while i > 0:
        if (i % 2 != 0):
            aux1 = d * b + c * a
            aux2 = d * (b + a) + c * b
            a, b = aux1, aux2
        aux1 = c ** 2 + d ** 2
        aux2 = d * (2 * c + d)
        c, d = aux1, aux2
        i //= 2
    return a + b


def sum_divisible_by(n: int, limit: int) -> int:
    '''
    Return the sum of all integers divisible by n up to limit.

    :param n: int
    :param limit: int

    :target = n // limit

    :return int n * (target * (target + 1)) // 2
    '''
    target = limit // n
    return n * (target * (target + 1)) // 2


def sieve_of_eratosthenes(limit=100) -> list:
    '''Return a list with all prime numbers below the limit.'''
    limit = abs(limit)
    if limit < 2:
        return []

    max_num_to_check = int(sqrt(limit)) + 1
    all_numbers = [x for x in range(3, limit, 2)]  # Get only odd numbers
    index = 0
    while True:
        number_being_checked = all_numbers[index]
        all_numbers = [x for x in all_numbers
                       if x == number_being_checked
                       or x % number_being_checked != 0]
        index += 1
        next_prime = all_numbers[index]
        if next_prime > max_num_to_check:
            all_numbers.insert(0, 2)  # Insert 2 at index 0
            return all_numbers


def factorial(num: int) -> int:
    num = abs(num)
    if num in (0, 1):
        return 1
    return num * factorial(num - 1)


def fib(f1=0, f2=1, limit=100) -> list:
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


def simple_combination(n: int, p: int) -> float:
    fact_n = factorial(n)
    fact_p = factorial(p)
    fact_np = factorial(n - p)
    return fact_n / (fact_p * fact_np)


def is_one_through_n_pandigital(number_to_check: int, n: int) -> bool:
    '''
    Check if a number is pandigital from 1 to n.

    Args:
        number_to_check: an integer with no more then 9 digits.
        n: the size of the pangidital number, from 1 to 9
    '''
    number_to_check = ''.join(sorted(str(number_to_check)))
    all_nums = string.digits[1:n + 1]  # Concatenated string with numbers 1..n
    return number_to_check == all_nums


def max_path_sum(triangle: list) -> int:
    triangle.reverse()
    for row_index, row in enumerate(triangle[1:]):
        for num_index, num in enumerate(row):
            left_sum = num + triangle[row_index][num_index]
            right_sum = num + triangle[row_index][num_index + 1]
            triangle[row_index + 1][num_index] = max(left_sum, right_sum)
    return triangle[-1]
