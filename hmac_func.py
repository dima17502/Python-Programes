from hashlib import sha256
import secrets
from matplotlib import pyplot as plt
import sys
from math import ceil

BLOCK_SIZE = 64
BITS_IN_BYTE = 8
SALT_SIZE = 32
ZERO_BYTE = (0).to_bytes(1, sys.byteorder)
Opad = '5c'
Ipad = '36'
OPAD_BLOCK = bytes.fromhex(Opad * BLOCK_SIZE)
IPAD_BLOCK = bytes.fromhex(Ipad * BLOCK_SIZE)
INT_OPAD_BLOCK = int.from_bytes(OPAD_BLOCK, sys.byteorder)
INT_IPAD_BLOCK = int.from_bytes(IPAD_BLOCK, sys.byteorder)

def hmac_sha256(key, message):
    key = sha256(key).digest()
    int_key = int.from_bytes(key, sys.byteorder)
    xor1 = (int_key ^ INT_OPAD_BLOCK).to_bytes(BLOCK_SIZE, sys.byteorder)
    xor2 = (int_key ^ INT_IPAD_BLOCK).to_bytes(BLOCK_SIZE, sys.byteorder)
    xor2_with_message = xor2 + message
    hashed_xor2_wm = sha256(xor2_with_message).digest()
    return sha256(xor1 + hashed_xor2_wm).digest()


def hkdf_extract(xts, skm):
    return hmac_sha256(xts, skm)


def hkdf_expand(prk, last_key, ctx, i):
    if last_key is None or i == 1:
        return hmac_sha256(prk, ctx + ZERO_BYTE)
    else:
        return hmac_sha256(prk, last_key + ctx + (i).to_bytes(ceil(i.bit_length() / BITS_IN_BYTE), sys.byteorder))


with open('weather.json', "rb") as f:
    binary_file = f.read()
    skm = sha256(binary_file).digest()

xts = (secrets.randbits(SALT_SIZE)).to_bytes(ceil(SALT_SIZE / BITS_IN_BYTE), sys.byteorder)
ctx = bytes('Dimetry', 'utf-8')
prk = hkdf_extract(xts, skm)
keys = [None]
for i in range(1, 1001):
    keys.append(hkdf_expand(prk, keys[i - 1], ctx, i))

plt.hist([keys[i][0] for i in range(1, len(keys))])
plt.title("Byte value distribution")
plt.xlabel("Byte values")
plt.ylabel("Occurence")
plt.show()