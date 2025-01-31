def tonelli_shanks(n, p):
    if pow(n, (p - 1) // 2, p) != 1:
        return -1

    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1

    if s == 1:
        return pow(n, (p + 1) // 4, p)

    z = 2
    while pow(z, (p - 1) // 2, p) == 1:
        z += 1

    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s

    while t != 0 and t != 1:
        i, t2 = 0, t

        while t2 != 1:
            t2 = pow(t2, 2, p)
            i += 1

        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i

    return r
