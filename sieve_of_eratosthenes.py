
n = int(input())

f = 2 == 2
sieve = [True] * (n + 1)
i = 2
while i * i <= n:
    j = i * i
    while j <= n:
        if sieve[j] and j % i == 0:
            sieve[j] = False
        j += i
    i += 1
for i in range (2, len(sieve)):
    if sieve[i]:
        print(i, end=' ')
