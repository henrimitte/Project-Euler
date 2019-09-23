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

print(sieve_of_eratosthenes())
