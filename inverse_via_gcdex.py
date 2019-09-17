

def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


def gcdex(a, b):
    flag = 0
    if a < b:
        (a, b) = (b, a)
        flag = 1
    if gcd(a, b) != 1:
        print("Reversed element doesn't exist")
        return 0
    r1 = a % b
    x1 = 1
    q1 = a // b
    y1 = -q1
    if r1 == 0:
        if flag == 0:
            return x1
        return y1
    q2 = b // r1
    r2 = b % r1
    x2 = -q2
    y2 = q1 * q2 + 1
    if r2 == 0:
        if flag == 0:
            return y2
        return y2
    r3 = r1 % r2
    while r3 != 0:
        q_t = r1 // r2
        a_t = -q_t * x2 + x1
        b_t = -q_t * y2 + y1
        r1 = r2
        r2 = r3
        q1 = q2
        q2 = q_t
        x1 = x2
        y1 = y2
        x2 = a_t
        y2 = b_t
        r3 = r1 % r2
    if flag == 0:
        return x2
    return y2


m, n = map(int, input().split())
print(gcdex(m, n))





