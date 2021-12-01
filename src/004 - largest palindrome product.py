def palindrome(num):
    n = [x for x in str(num)]
    pal = n.copy()
    pal.reverse()
    return n == pal

biggest = 0
for c in range(999, 99, -1):
    for d in range(999, 99, -1):
        m = c * d
        if palindrome(m):
            if m > biggest:
                biggest = m

print(biggest)
