endless_loop = (1, 89)
end_in_eighty_nine = 0

def get_sum_of_the_squares_of_the_digits(number):
    return sum([pow(int(x), 2) for x in str(number)])

for i in range(1, 10000000):
    actual_number = i
    while True:
        next_number_of_the_chain = get_sum_of_the_squares_of_the_digits(actual_number)
        if next_number_of_the_chain in endless_loop:
            if next_number_of_the_chain == 89:
                end_in_eighty_nine += 1
            break
        actual_number = next_number_of_the_chain

print(end_in_eighty_nine)
