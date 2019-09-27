one_to_nine = ('one', 'two', 'three',
               'four', 'five', 'six',
               'seven', 'eight', 'nine')
eleven_to_nineteen = ('eleven', 'twelve', 'thirteen',
                      'fourteen', 'fifteen', 'sixteen',
                      'seventeen', 'eighteen', 'nineteen')
dezens = ('ten', 'twenty', 'thirty',
          'fourty', 'fifty', 'sixty',
          'seventy', 'eighty', 'ninety')
hundreds = [x + 'hundred' for x in one_to_nine]

one_to_nine_len = [len(x) for x in one_to_nine]
print(one_to_nine_len)
