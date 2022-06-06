'''              
    доработать: 
    - проверка пользовательского ввода, что число от 1 до 100 вкл


    
'''




import random
from math import log, ceil

def get_user_number(left_border, right_border):
    pass    
def get_user_input(case):
    pass
def get_attempts_by_mode(n):
    pass

def guess_number():
    print("Enter min positive number I can choose:")
    left_border = int(input())
    print("Enter max positive number I can choose:")
    right_border = int(input())
    h_tries = ceil(log(right_border - left_border, 2))
    m_tries = int(h_tries *1.5)
    e_tries = int(h_tries * 2)
    print( f"I chose a number between {left_border} and {right_border} including borders.",
           "Can you guess it?")
    print("There are 3 levels for this game. \n" +
          f"On easy level(1) you have {e_tries} attempts to guess a number\n"+
          f"On medium(2) - {m_tries} attempts\n" +f"On hard(3) level - {h_tries}")
    print("Which one you choose? Press 1, 2 or 3")
    attempts = 0
    mode = int(input())
    if mode == 1:
        attempts = e_tries
    elif mode == 2:
        attempts = m_tries
    elif mode == 3:
        attempts = h_tries
    
    user_wish = 'c'
    while user_wish == 'c':
        n = random.randrange(left_border, right_border + 1)
        c_attempt = 0
        user_guess = n + 1
        while user_guess != n and c_attempt != attempts:
            print(f"Attempt {c_attempt +1}/{attempts}")
            print(f"Type a number in range from {left_border} to {right_border}: ")
            user_guess = int(input())
            if user_guess > n:
                print("Too much. Try again.")
            elif user_guess < n:
                print("Too little. Try again.")  
            else:
                print("Congratulations! This is it!")
            c_attempt += 1
        if user_guess == n:
            print( "Press 'n' to start new game, 'c' to continue with same parameters or 'q' то quit")    
        else:
            print("Attempts are over.\n" +
          "Press 'n' to start new game, 'c' to continue with same parameters or 'q' то quit")
        user_wish = input()
        if user_wish =='n':
            guess_number()
        elif user_wish =='q':
            print("Bye!")
guess_number()
