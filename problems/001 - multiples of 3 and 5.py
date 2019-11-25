divs_list = []
for c in range(1, 1000):
    if c % 3 == 0 or c % 5 == 0:
        divs_list.append(c)

print(sum(divs_list))
