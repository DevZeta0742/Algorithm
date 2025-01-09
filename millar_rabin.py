import random

def is_prime(n: int):
    pil = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    if n == 1:
        return False

    if n in pil:
        return True

    for a in pil:
        if not millar_rabin(n, a):
            return False

    return True


def millar_rabin(n: int, k: int):
    if n == 2:
        return True

    if n % 2 == 0 or n <= 1:
        return False

    s = 0
    d = n - 1

    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True
