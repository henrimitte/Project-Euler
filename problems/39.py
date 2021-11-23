def hipotenuse(a, b):
    return ((a**2) + (b**2)) ** 0.5


perimeters = {x: 0 for x in range(3, 1001)}
possible = True
a = b = 0
while possible:
    a += 1
    b, h = a, hipotenuse(a, b)
    p = a + b + h
    if p > 1000:
        possible = False
    while p <= 1000:
        if p == int(p):
            perimeters[p] += 1
            # print(a, b, h, p)
        b += 1
        h = hipotenuse(a, b)
        p = a + b + h

biggest = max(perimeters.keys(), key=lambda x: perimeters[x])
print(biggest, perimeters[biggest])
