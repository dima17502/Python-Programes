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


n = int(input())
fact_list = factors(n)
print(*fact_list)
