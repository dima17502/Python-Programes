from math import sqrt


def is_prime(n):
    i = 2
    while i < sqrt(n) + 1 and n % i != 0:
        i += 1
    return n % i != 0


def factors(n):
    res = []
    while n > 1:
        i = 2
        while i < sqrt(n) + 1 and n % i != 0:
            i += 1
        if n % i == 0:
            res.append(i)
            n //= i
        else:
            res.append(n)
            n = 1
    return res


def euler_func(fact_list):
    fact_dict = {}
    for i in fact_list:
        fact_dict[i] = fact_dict.get(i, 0) + 1
    res = 1
    for i in fact_dict:
        res *= (i**fact_dict[i] - i**(fact_dict[i] - 1))
    return res


def exponentiation(exponent, power):
    if power == 0:
        return 1
    elif power % 2 == 1:
        return exponent * exponentiation(exponent, power - 1)
    else:
        half = exponentiation(exponent, power // 2)
        return half * half


def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


m = int(input())
print("Element    Reverse Element ")
if is_prime(m):
    for i in range(1, m):
        j = exponentiation(i, m - 2) % m
        print('{0:5d}{1:12d}'.format(i, j))
else:
    for i in range(1, m):
        if gcd(i, m) == 1:
            j = exponentiation(i, euler_func(factors(m)) - 1) % m
            print('{0:5d}{1:12d}'.format(i, j))
