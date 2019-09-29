
n = int(input())

sieve = [True] * (n + 1)
i = 2
count = 0
while i * i <= n:
    j = i * i
    if sieve[j]:
        while j <= n:
            sieve[j] = False
            j += i
    i += 1
for i in range (2, len(sieve)):
    if sieve[i]:
        count += 1
        #print(i, end=' ')
print(count)
