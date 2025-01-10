from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 50
getcontext().rounding = ROUND_HALF_UP

pi = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')

def sin(i: Decimal) -> Decimal:
    i = i % (2 * pi)
    n = Decimal(1)
    tmp = Decimal(i)
    p = Decimal(i)

    while abs(tmp) >= Decimal('1e-40'):
        n += 2
        fac = n * (n - 1)
        tmp = (tmp * i * i) / -fac
        p += tmp

    return p

def cos(i: Decimal) -> Decimal:
    i = i % (2 * pi)
    n = Decimal(0)
    tmp = Decimal(1)
    p = Decimal(1)

    while abs(tmp) >= Decimal('1e-40'):
        n += 2
        fac = n * (n - 1)
        tmp = (tmp * i * i) / -fac
        p += tmp

    return p

def tan(i: Decimal) -> Decimal:
    sin_val = sin(i)
    cos_val = cos(i)

    if cos_val == 0:
        raise ValueError("cos(i) is zero, tan(i) is undefined")

    res = sin_val / cos_val

    return res

a = Decimal(input())
print(f"sin(a) = {sin(a)}")
print(f"cos(a) = {cos(a)}")
print(f"tan(a) = {tan(a)}")
