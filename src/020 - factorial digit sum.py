from tools import factorial

n = [int(x) for x in str(factorial(100))]
soma = 0
for num in n:
    soma += num

print(soma)
