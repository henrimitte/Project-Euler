numQuad = somaQuad = 0
for c in range(1, 101):
    numQuad += pow(c, 2)
    somaQuad += c

somaQuad = pow(somaQuad, 2)
print(somaQuad - numQuad)
