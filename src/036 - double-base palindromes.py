'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def is_base_10_palindrome(num: int) -> bool:
    reversed_num = ''.join([x for x in reversed(str(num))])
    return num == int(reversed_num)

def is_base_2_palindrome(num: int) -> bool:
    binary = str(bin(num))[2:]
    reversed_num = ''.join([x for x in reversed(str(binary))])
    return int(binary) == int(reversed_num) 

total = 0
for c in range(1, 1000000):
    is_double_palindrome = is_base_2_palindrome(c) and is_base_10_palindrome(c)
    if is_double_palindrome:
        total += c

print(total)