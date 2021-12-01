'''145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.'''

from tools import factorial


sum_of_factorials = 0
for number in range(3, 2540161):
    all_fact = [factorial(int(x)) for x in str(number)]
    if number == sum(all_fact):
        sum_of_factorials += number

print(sum_of_factorials)
