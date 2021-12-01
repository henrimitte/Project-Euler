from tools import sieve_of_eratosthenes

primes = sieve_of_eratosthenes(800000)


def left_to_right(n):
    n = str(n)
    for a in range(1, len(n)):
        if int(n[a:]) not in primes:
            return False
    return True


def right_to_left(n):
    n = str(n)
    for a in range(1, len(n)):
        if int(n[:-a]) not in primes:
            return False
    return True


s = found = 0
index = 5
while found < 11:
    p = primes[index]
    lr = left_to_right(p)
    rl = right_to_left(p)
    if lr and rl:
        print(p)
        s += p
        found += 1
    index += 1

print(s)
