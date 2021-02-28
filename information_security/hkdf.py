from hashlib import sha256
import secrets
from math import ceil
import sys
from matplotlib import pyplot

def to_bytes1(obj, size):
    return obj.to_bytes(size, sys.byteorder)

BlockSize = 64
Opad = '5c'
Ipad = '36'
BitsInByte = 8
OpadBlock = bytes.fromhex(Opad * BlockSize)
IpadBlock = bytes.fromhex(Ipad * BlockSize)
ZeroByte = to_bytes1(0, 1)
SaltSize = 32

def bxor(b1, b2):
    parts = []
    for b1, b2 in zip(b1, b2):
        parts.append(bytes([b1 ^ b2]))
    return b''.join(parts)

def HmacSha256(key, mess):
    key = sha256(key).digest()
    opadxor = bxor(key,OpadBlock)
    ipadxor = bxor(key, IpadBlock)
    cont1 = sha256(ipadxor + mess).digest()
    return sha256(opadxor + cont1).digest()

def HkdfExtract(xts, skm):
    return HmacSha256(xts, skm)

def HkdfExpand(prk, lastKey, ctx, i):
    if lastKey is None or i == 1:
        return HmacSha256(prk, ctx + ZeroByte)
    else:
        ibyte = to_bytes1(i, ceil(i.bit_length() / BitsInByte))
        return HmacSha256(prk, lastKey + ctx + ibyte)

weather_json = open("weather.json", "rb")
skm = sha256(weather_json.readline()).digest()
weather_json.close()

xts = to_bytes1(secrets.randbits(SaltSize), ceil(SaltSize / BitsInByte))
ctx = bytes('Kirill', 'utf-8')
prk = HkdfExtract(xts, skm)
keys = [None]
for i in range(1, 1001):
    keys.append(HkdfExpand(prk, keys[i-1], ctx, i ))

pyplot.hist([keys[i][0] for i in range(1, len(keys))])
pyplot.title("Byte value histogram")
pyplot.xlabel("Byte values")
pyplot.ylabel("Frequency")
pyplot.show()
