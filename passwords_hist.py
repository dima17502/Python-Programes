import requests
import json
from matplotlib import pyplot as plt

response = requests.get('https://raw.githubusercontent.com/CryptoCourse/CryptoLabs/master/Impl/passwords.json')
passwords = json.loads(response.text)

binary_passwords = list(map(lambda x: bin(int.from_bytes(x.encode(), 'big')), passwords))
first_bits = [password[2:7] for password in binary_passwords]

plt.hist(first_bits)
plt.title("Histogram for first 5 bites in passwords")
plt.xlabel("Bits")
plt.ylabel("Occurence")
plt.show()
