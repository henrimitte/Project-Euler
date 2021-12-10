from tools import sum_of_ints


def solve():
    triangle_numbers = tuple(sum_of_ints(x) for x in range(1, 20))
    upper_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_values = {upper_alpha[x]: x + 1 for x in range(0, 26)}

    with open('ext_files/p042_words.txt', 'r') as arq:
        all_words = arq.read().replace('"', '').split(',')
        t_words = 0
        for word in all_words:
            s = sum(alpha_values[ch] for ch in word)
            if s in triangle_numbers:
                t_words += 1

    print(t_words)


if __name__ == '__main__':
    solve()
