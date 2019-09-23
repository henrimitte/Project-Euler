sum = 0
for c in range(1, 1000):
    if (c % 3 == 0) or (c % 5 == 0):
        sum += c

print(sum)
