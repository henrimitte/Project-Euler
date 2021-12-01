'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def collatz(num: int):
    seq = [num]
    while num > 1:
        par = num % 2 == 0
        num = int(num / 2) if par else int(num * 3 + 1)
        seq.append(num)
    return len(seq)


biggest = 0
index = 0
for c in range(3, 1000000):
    n = collatz(c)
    if n > biggest:
        biggest = n
        index = c

print(index, biggest)
