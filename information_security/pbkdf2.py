from hashlib import sha256
import secrets
from matplotlib import pyplot as plt
import requests
import json
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
ITERATIONS = 10000
KEY_LEN = 512

def hmac_sha256(key, message):
    key = sha256(key).digest()
    int_key = int.from_bytes(key, sys.byteorder)
    xor1 = (int_key ^ INT_OPAD_BLOCK).to_bytes(BLOCK_SIZE, sys.byteorder)
    xor2 = (int_key ^ INT_IPAD_BLOCK).to_bytes(BLOCK_SIZE, sys.byteorder)
    xor2_with_message = xor2 + message
    hashed_xor2_wm = sha256(xor2_with_message).digest()
    return sha256(xor1 + hashed_xor2_wm).digest()


def pbkdf2(password, salt, c, key_size):
    t = ZERO_BYTE
    blocks_amount = ceil(key_size / (BLOCK_SIZE / 2 * BITS_IN_BYTE))
    for j in range(blocks_amount):
        u = hmac_sha256(password, salt + (j + 1).to_bytes(ceil((j + 1).bit_length() / BITS_IN_BYTE), sys.byteorder))
        u_previous = u
        for i in range(1, c):
            u_i = hmac_sha256(password, u_previous)
            int_u = int.from_bytes(u, sys.byteorder)
            int_u_i = int.from_bytes(u_i, sys.byteorder)
            u_i = (int_u ^ int_u_i).to_bytes(BLOCK_SIZE // 2, sys.byteorder)
            u_previous = u_i
        if j == 0:
            t = u
        else:
            t += u
    return t


response = requests.get('https://raw.githubusercontent.com/CryptoCourse/CryptoLabs/master/Impl/passwords.json')
passwords = json.loads(response.text)

salt = (secrets.randbits(SALT_SIZE)).to_bytes(ceil(SALT_SIZE / BITS_IN_BYTE), sys.byteorder)
keys = []
for password in passwords:
    keys.append(pbkdf2(bytes(password, 'utf-8'), salt, ITERATIONS // 10, KEY_LEN))

bytes_passw = [x[0] for x in keys]
plt.hist(bytes_passw)
plt.title("Histogram for  first bits of password key")
plt.xlabel("bits")
plt.ylabel("Occurency")
plt.show()
