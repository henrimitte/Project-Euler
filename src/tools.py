import string
from math import sqrt, log


def get_nth_pentagonal(nth: int) -> int:
    '''
    Return the nth pentagonal number.

    :param nth: int

    :return int nth * (3 * nth - 1) // 2
    '''
    return nth * (3 * nth - 1) // 2


def sum_digits_of_n(n: int) -> int:
    '''
    Return the sum of all the digits on n.

    :param n: int

    :return int
    '''
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def get_nth_ordered_permutation(nth: int, size: int = None) -> int:
    '''
    Return the nth ordered permutation of size.

    :param nth: int
    :param size: int

    :return int
    '''
    nums = list('0123456789')
    nth -= 1
    final = ''
    size = 10 if size is None else size
    for c in range(size - 1, -1, -1):
        f = factorial(c)
        d, m = divmod(nth, f)
        final += nums.pop(int(d))
        nth = m

    return int(final)


def least_common_multiple(a: int, b: int) -> int:
    '''
    Return the least common multiple of a and b for a > 0 and b > 0.

    :param a: int
    :param b: int

    :return int
    '''
    return abs(a * b) // greatest_common_divisor(a, b)


def greatest_common_divisor(a: int, b: int) -> int:
    '''
    Return the greatest common divisor of a and b for a > 0 and b > 0.

    :param a: int
    :param b: int

    :return int
    '''
    while True:
        a, b = b, a % b
        if b == 0:
            return a


def get_pythagorean_triplet(m: int, n: int) -> tuple:
    '''
    Return a primitive pythagorean triplet for any integers m, n, with m > n.

    :param m: int
    :param n: int

    :return tuple(a: int, b: int, c: int)
    '''
    if m <= n:
        return ()
    m_sqrd, n_sqrd = m ** 2, n ** 2
    a = m_sqrd - n_sqrd
    b = 2 * m * n
    c = m_sqrd + n_sqrd
    return a, b, c


def sum_of_ints(n: int) -> int:
    '''
    Return the sum of all integers from 1 up to n.

    :param n: int

    :return int n * (n + 1) // 2
    '''
    return n * (n + 1) // 2


def sum_of_squares(n: int) -> int:
    '''
    Return the sum of the squares of 1 up to n.

    :param n: int

    :return int (n * (n + 1) * (2 * n + 1)) // 6
    '''
    return (n * (n + 1) * (2 * n + 1)) // 6


def smallest_divisible_from_1_to_n(n: int) -> int:
    '''
    Return the smallest number divisible from 1 up to n.

    :param n: int
    '''
    i, k = 0, 1
    check = True
    limit = int(sqrt(n))
    a = [0 for _ in range(n)]
    primes = sieve_of_eratosthenes(n ** 2)
    while primes[i] <= n:
        a[i] = 1
        if check:
            if primes[i] <= limit:
                a[i] = int(log(n) // log(primes[i]))
            else:
                check = False
        k = k * primes[i] ** a[i]
        i += 1
    return k


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
    if 0 >= num <= 1:
        return 1
    m = 1
    for c in range(2, num + 1):
        m *= c
    return m


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


def is_one_to_n_pandigital(n: str, size: int) -> bool:
    '''
    Check if a number is pandigital from 1 to n.

    :param n: str
    :param size: int

    :return bool
    '''
    return ''.join(sorted(n)) == string.digits[1:size + 1]


def max_path_sum(triangle: list) -> int:
    '''
    Return the max sum of a path of a triangle.

    :param triangle: list
    '''
    triangle.reverse()
    for row_index, row in enumerate(triangle[1:]):
        for num_index, num in enumerate(row):
            left_sum = num + triangle[row_index][num_index]
            right_sum = num + triangle[row_index][num_index + 1]
            triangle[row_index + 1][num_index] = max(left_sum, right_sum)
    return triangle[-1][0]
