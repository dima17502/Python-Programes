

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
        d, x, y = gcdex(b, a)
        return d, y, x
    else:
        print("Invalid input")
        return -1


def inv_elem(a, b):
    d, x, y = gcdex(a, b)
    if gcdex(a, b)[0] == 1:
        return d, x
    print("Inverse element doesn't exist")
    return -1


m, n = map(int, input().split())
print(inv_elem(m, n))




