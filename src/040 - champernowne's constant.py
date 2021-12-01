s = ''
c = soma = start = 1
while len(s) < 1000001:
    s += str(c)
    c += 1
while start < 1000001:
    soma *= int(s[start - 1])
    start *= 10

print(soma)
