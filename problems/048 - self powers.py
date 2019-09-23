s = 0
for c in range(1, 1001):
    s += pow(c, c)
print(str(s)[-10:])