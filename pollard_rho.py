from math import gcd

def pollard_rho(n: int):
    if n % 2 == 0:
        return 2

    if is_prime(n):
        return n

    if n == 1:
        return 1

    x = random.randint(1, n - 1)
    y = x
    c = random.randint(1, n - 1)
    g = 1

    while g == 1:
        x = ((x * x) % n + c) % n
        y = ((y * y) % n + c) % n
        y = ((y * y) % n + c) % n
        g = gcd(abs(x - y), n)

        if g == n:
            return pollard_rho(n)

    if is_prime(g):
        return g

    else:
        return pollard_rho(g)


def prime_factor(n: int):
    if n == 1:
        return []

    if is_prime(n):
        return [n]

    x = pollard_rho(n)

    return prime_factor(x) + prime_factor(n // x)
