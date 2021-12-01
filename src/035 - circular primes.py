'''The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?'''

from TOOLS import sieve_of_eratosthenes


def rotate_number(num):
    rotated_nums = [num]
    num = str(num)
    rotations = len(num) - 1
    all_nums_are_equal = all([x == num[0] for x in num])

    if rotations == 0 or all_nums_are_equal:
        return rotated_nums

    for _ in range(rotations):
        digits = [x for x in num]
        last_num = digits[-1]
        digits.pop(-1)
        digits.insert(0, last_num)
        num = ''.join(digits)
        rotated_nums.append(int(num))

    return rotated_nums

print('Gathering prime numbers below one million...')
primes_below_one_million = sieve_of_eratosthenes(1000000)
print('Done!')
max_num_to_check = sorted(rotate_number(primes_below_one_million[-1]))[0]
print(f'Biggest number to check: {max_num_to_check}')

index = 0
while True:
    number_being_checked = primes_below_one_million[index]
    if number_being_checked > max_num_to_check:
        break
    rotated = rotate_number(number_being_checked)
    are_all_primes = all([x in primes_below_one_million for x in rotated])
    if not are_all_primes:
        primes_below_one_million = [x for x in primes_below_one_million if x not in rotated]
    else:
        index += 1

print(len(primes_below_one_million))
