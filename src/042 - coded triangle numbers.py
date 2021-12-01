import string

def generate_triangle_number(nth):
    return int(0.5 * nth * (nth + 1))

triangle_numbers = [generate_triangle_number(x) for x in range(1, 50)]
alphanum = {string.ascii_uppercase[x]:x + 1 for x in range(0, 26)}
with open('p042_words.txt', 'r') as arq:
    all_words = arq.read().replace('"', '').split(',')
    t_words = 0
    for index, word in enumerate(all_words, start=1):
        soma = 0
        for letter in word:
            soma += alphanum[letter]
        if soma in triangle_numbers:
            t_words += 1

print(t_words)
