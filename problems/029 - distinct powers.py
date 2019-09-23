dist_pwr = []

for c in range(2, 101):
    for d in range(2, 101):
        m = c * d
        if m not in dist_pwr:
            dist_pwr.append(m)

print(len(dist_pwr))
