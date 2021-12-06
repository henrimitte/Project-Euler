from tools import get_nth_fibonacci


length = i = 0
while length < 1000:
    i += 1
    length = len(str(get_nth_fibonacci(i)))

print(i)
