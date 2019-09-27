def get_sum_of_divisors(num):
    divisors = []
    for c in range(1, (num // 2) + 1):
        if num % c == 0:
            divisors.append(c)
    soma = 0
    for n in divisors:
        soma += n
    return soma

nums = [x for x in range(2, 10000)]
amicable = []
for n in nums.copy():
    sum_of_num_divisors = get_sum_of_divisors(n)
    div_of_div = get_sum_of_divisors(sum_of_num_divisors)
    is_amicable = (n == div_of_div and n != sum_of_num_divisors)
    if is_amicable:
        amicable.append(n)

s = 0
for num in amicable:
    s += num
print(s)
