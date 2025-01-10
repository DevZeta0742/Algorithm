# 1 recursive function - O(2^n)
def fibonacci(n):
    if n == 1:
        return 1

    elif n == 2:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)


# 2 dp - O(n)
dp = [0] * 100  # space complexity O(n)
dp[1] = 1
dp[2] = 1

for i in range(3, 100):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[99])


def fibonacci_optimized(n): # space complexity O(1)
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


# matrix exponentiation - O(log n)
def multiply(F, M):
    x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
    y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
    z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
    w = F[1][0] * M[0][1] + F[1][1] * M[1][1]

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F, n):
    if n == 0 or n == 1:
        return

    M = [[1, 1], [1, 0]]
    power(F, n // 2)
    multiply(F, F)

    if n % 2 != 0:
        multiply(F, M)

def fibonacci(n):
    F = [[1, 1], [1, 0]]

    if n == 0:
        return 0

    power(F, n - 1)

    return F[0][0]

# Binet's formula - O(1)
import decimal
decimal.getcontext().prec = 30000  # 숫자 클수록 더 정확하게 계산함
# __import__('sys').set_int_max_str_digits(250000)

def Binet(n):
    sqrt5 = decimal.Decimal(5).sqrt()
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2

    return round((phi ** n - psi ** n) / sqrt5)

print(int(Binet(1000000)))
