from TOOLS import max_path_sum

triangle = []
with open('problems\p067_triangle.txt') as arq:
    for row in arq.readlines():
        triangle.append([int(x) for x in row.split(' ')])

print(max_path_sum(triangle))
