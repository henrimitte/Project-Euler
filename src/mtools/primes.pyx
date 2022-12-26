def soa_nums(unsigned long int limit = 20) -> list:
    if limit < 2:
        return []
    elif limit == 2:
        return [2]
    elif limit == 3:
        return [2, 3]

    cdef list result = [2, 3, 5]
    if limit == 5:    
        return result

    cdef list sieve = [False] * (limit + 1)
    cdef unsigned long int x, x2, y, y2, n, r, r2
    x = 1
    x2 = x * x
    while x2 < limit:
        y = 1
        y2 = y * y
        while y2 < limit:
            n = (4 * x2) + y2
            if (n <= limit and (n % 12 == 1 or n % 12 == 5)):
                sieve[n] ^= True

            n = (3 * x2) + y2
            if (n <= limit and (n % 12 == 7)):
                sieve[n] ^= True

            n = (3 * x2) - y2
            if x > y and (n <= limit) and (n % 12 == 11):
                sieve[n] ^= True
            y += 1
            y2 = y * y
        x += 1
        x2 = x * x

    r = 5
    r2 = r * r
    while r2 < limit:
        if sieve[r]:
            for i in range(r2, limit, r2):
                sieve[i] = False
        r += 1
        r2 = r * r

    return result + [x for x in range(7, limit, 2) if sieve[x]]
