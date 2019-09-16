from math import sqrt


def is_prime(n):
    i = 2
    while i < sqrt(n) + 1 and n % i != 0:
        i += 1
    return n % i != 0


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
if is_prime(m):                                  #when modul is prime all elements of the ring have inverse element
    for i in range(1, m):
        j = 1
        while (i * j) % m != 1:
            j += 1
        print('{0:5d}{1:12d}'.format(i, j))
else:
    for i in range(1, m):
        if gcd(i, m) == 1:
            j = 1
            while (i * j) % m != 1:
                j += 1
            print('{0:5d}{1:12d}'.format(i, j))





