from math import log2, ceil

p = 998244353

def fft(a: list, inv: bool):
    n = len(a)
    j = 0

    for i in range(1, n):
        rev = n // 2

        while j >= rev:
            j -= rev
            rev //= 2

        j += rev

        if i < j:
            a[i], a[j] = a[j], a[i]

    step = 2
    while step <= n:
        half = step // 2
        u = pow(3, p // step, p)

        if inv:
            u = pow(u, p - 2, p)

        for i in range(0, n, step):
            w = 1

            for j in range(i, i + half):
                v = a[j + half] * w % p
                a[j + half] = (a[j] - v) % p
                a[j] = (a[j] + v) % p
                w = w * u % p

        step *= 2

    if inv:
        num = pow(n, p - 2, p)

        for i in range(n):
            a[i] = a[i] * num % p

def multiply_polynomials(A: list, B: list): # 다항식 곱
    n = 1 << ceil(log2(len(A) + len(B) - 1))

    a = A + [0] * (n - len(A))
    b = B + [0] * (n - len(B))

    fft(a, False)
    fft(b, False)

    c = [(a[i] * b[i]) % p for i in range(n)]
    fft(c, True)

    return c
