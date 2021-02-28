


def gcdex(a, b):
    if a >= b >= 0 and a + b > 0:
        if b == 0:
            d, x, y = (a, 1, 0)
        else:
            d, p, q = gcdex(b, a % b)
            x = q
            y = p - (a // b) * q
        return d, x, y
    elif  b > a > 0:
        d, x, y = gcdex(b,a)
        return d, y, x
    else:
        print("Invalid input")
        return -1



m, n = map(int, input().split())
print(gcdex(m, n))




