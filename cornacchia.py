def cornacchia(n):
    if n % 4 == 3:
        return False

    if n == 2:
        return 1

    r1 = tonelli_shanks(n-1, n)
    r2 = n

    while r1 ** 2 > n:
        r2 %= r1

        if r2 ** 2 < n:
            return r2

        r1 %= r2

    return r1
