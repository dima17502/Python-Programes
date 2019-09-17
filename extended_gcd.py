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


def gcdex(a, b):
    if a < b:
        (a, b) = (b, a)
    r1 = a % b
    a1_i = 1
    q1 = a // b
    b1_i = -q1
    if r1 == 0:
        return a1_i, -b1_i + 1, b
    q2 = b // r1
    r2 = b % r1
    a2_i = -q2
    b2_i = q1 * q2 + 1
    if r2 == 0:
        return a2_i, b2_i, r1
    r3 = r1 % r2
    while r3 != 0:
        q_t = r1 // r2
        a_t = -q_t * a2_i + a1_i
        b_t = -q_t * b2_i + b1_i
        r1 = r2
        r2 = r3
        q1 = q2
        q2 = q_t
        a1_i = a2_i
        b1_i = b2_i
        a2_i = a_t
        b2_i = b_t
        r3 = r1 % r2
    return a2_i, b2_i, r2


m, n = map(int, input().split())
print(*gcdex(m, n))




