from math import sqrt


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
            res.append(n)   # when number is prime
            n = 1
    return res


def euler_func(fact_list):
    fact_dict = {}
    for i in fact_list:
        fact_dict[i] = fact_dict.get(i, 0) + 1
    res = 1
    for i in fact_dict:
        res *= (i**fact_dict[i] - i**(fact_dict[i] - 1))        #use multiplicative property of the function
    return res


n = int(input())
fact_list = factors(n)
print(euler_func(fact_list))
