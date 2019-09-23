fifth_pwr = []
for c in range(2, 1000000):
    l = [int(x) for x in str(c)]
    s = 0
    for n in l:
        s += pow(n, 5)
    if s == c:
        fifth_pwr.append(c)

sm = 0
for n in fifth_pwr:
    sm += n
print(sm)
