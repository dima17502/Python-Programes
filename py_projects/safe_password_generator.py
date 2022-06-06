'''
Описание проекта: программа генерирует заданное количество паролей 
и включает в себя умную настройку на длину пароля, 
а также на то, какие символы требуется в него включить, а какие исключить.
защита от дурака должна включать в себя проверки:
что длина пароля больше нуля, ответы y или n, есть 'y',

'''

import random


def password_generator(amount,size, up, d, l, s, cs):
    con_let = "ilI1Lo0O"
    symbols = "!#$%&*+-=?@^_"
    charset = ""
    if up == 'y':
        alph = [chr(i + ord('A')) for i in range(26)]
        charset += ''.join(alph)
    if l == 'y':
        alph = [chr(ord('a') + i) for i in range(26)]
        charset += ''.join(alph)
    if d == 'y':
        alph = [str(i) for i in range(10) if chr(i)]
        charset += ''.join(alph)
    if s == 'y':
        charset += symbols
    if cs == 'y':
        temp = ""
        for c in charset:
            if c not in con_let:
                temp += c
        charset = temp
    passwords = []
    for i in range(amount):
        p = ""
        for j in range(size):
            p += random.choice(charset)
        passwords.append(p)
    return passwords
        



def main():
    amount = int(input("How much passwords do you need?"))
    size = int(input("What size of password do you want?"))
    up = input("Include capital letters in password?('A','B',..)\n" +
               "Print 'y' for yes and 'n' for no")
    d = input("Add digits to the password?(0,1..)\n" + 
              "Print 'y' for yes and 'n' for no")
    l = input("Include lowercase letters?(a,b,..)\n" +
              "Print 'y' for yes and 'n' for no")          
    s = input("Include symbols like '!#$%&*+-=?@^_') ?\n" +
              "Print 'y' for yes and 'n' for no")
    cs = input("Exclude confusing symbols like ilI1Lo0O ?\n" +
               "Print 'y' for yes and 'n' for no")
    passwords = password_generator(amount,size, up, d, l ,s, cs)
    print(*passwords,sep='\n')

main()