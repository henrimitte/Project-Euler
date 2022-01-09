def solve():
    digits = ['one', 'two', 'three', 'four',
              'five', 'six', 'seven', 'eight', 'nine']
    eleven_to_nineteen = ['eleven', 'twelve', 'thirteen', 'fourteen',
                          'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    dozens = ['ten', 'twenty', 'thirty', 'forty',
              'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    hundred = 'hundred'
    thousand = len('onethousand')
    a = 'and'

    total_digits = sum(len(w) * 90 for w in digits)
    total_ten = sum(len(w) * 10 for w in dozens[0])
    total_eleven_to_nineteen = sum(len(w) * 10 for w in eleven_to_nineteen)
    total_dozens = sum(len(w) * 100 for w in dozens[1:])
    total_hundred = sum(len(w + hundred) * 100 for w in digits)
    total_and = sum(len(a) * 99 for _ in digits)

    total = total_digits + total_ten + total_eleven_to_nineteen + \
        total_dozens + total_hundred + total_and + thousand

    print(total)


if __name__ == '__main__':
    solve()
