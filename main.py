import math


def fun(n,m):
    a = 0
    b = 0
    for i in range(1, n + 1):
        a = a + (i ** 5 - 68 * i ** 7 + 46)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            b = b + (i ** 7 - (i ** 6) / 13)

    result = 85 * a + 16 * b
    return result


print(f"{fun(10,44):.2e}")