from math import sqrt
for n in range(2, 1000):
    for m in range(2, 1000):
        a2 = n ** 2
        a = sqrt(a2)
        b2 = m ** 2
        b = sqrt(b2)
        c2 = a2 + b2
        c = sqrt(c2)
        if a < b < c and a + b + c == 1000:
            print(f'{int(a)}² + {int(b)}² + {int(c)}² =  {c2}')
