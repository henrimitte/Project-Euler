'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
import string


def is_one_through_n_pandigital(number_to_check, n = 5):
    all_nums = string.digits[1:n + 1] # String com todos os números de 1 até n
    return number_to_check == all_nums

list_of_products_to_sum = []
for c in range(2, 2000):
    for d in range(2, 2000):
        product = c * d
        concat = str(c) + str(d) + str(product)
        if len(concat) > 9:
            break
        str_sorted_and_concatenaded = ''.join(sorted([x for x in concat]))
        pandigital = is_one_through_n_pandigital(str_sorted_and_concatenaded, 9)
        if pandigital:
            if product not in list_of_products_to_sum:
                list_of_products_to_sum.append(product)

print(sum(list_of_products_to_sum))
