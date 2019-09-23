'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''
numbers = [x for x in range(1, 21)]

nume = 0
cont = 20
while True:
    booleans = []
    for n in numbers:
        booleans.append(cont % n == 0)
    if all(booleans):
        nume = cont
        break
    cont += 20
print(cont)
