'''
n человек, пронумерованных числами от 11 до nn, стоят в кругу. 
Они начинают считаться, каждый kk-й по счету человек выбывает из круга, 
после чего счет продолжается со следующего за ним человека. 
Напишите программу, определяющую номер человека, который останется в кругу последним.
'''


n, k = int(input()), int(input())
i = 2
res = 1
while i <= n:
    if (res + k) % i == 0:
        res = i
    else:
        res = (res + k) % i
    i += 1
print(res)
