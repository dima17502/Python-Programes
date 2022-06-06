'''


hard: 
 _________
|    |    |
|    O    |
|   /|\   |
|   / \   |
|         |
|         |
 ________
|   |    |
|   О    |
| ( | )  |
| _/ \_  |
|        |
|   П    |


 ________
|/  |   \|
|   O    |
|  (|)   |
| _/ \_  |
|        |
|   П    |

в режиме easy появляются использованные буквы
'''

import random

easy = ["кот", "ёж", "кит","коза", "мышь","крыса", "лев", "лось", "рыба", "змея","корова","собака","хомяк"]
medium = ["гепард", "голубь","удав", "гадюка","тритон","ящерица", "кабан","обезьяна","горилла", "утконос"]
hard = ["муравьед", "осьминог", "минога","журавль","тетерев","шимпанзе","орангутан",
        "баразубка", "кенгуру"]
word = [easy,medium, hard]


def hangman():
    lvl = int(input("Choose level. '1' for easy, '2' for medium and '3' for hard\n"))
    gw = word[lvl - 1][random.randint(0, len(word[lvl-1]) - 1)]
    guess = list("_"* len(gw))
    used_letters = ""
    g_l = 0
    attempts = [12, 9, 6]
    us_attempt = 0
    while us_attempt != attempts[lvl-1] and g_l != len(gw):
        print(f"Round {us_attempt + 1}/{attempts[lvl-1]}", ' '.join(guess),
              "\nType a letter: ")
        letter = input()
        t = gw.find(letter)
        if t!= -1 and guess[t] == '_':
            print("You are right!")
            for i in range(len(gw)):
                if gw[i] == letter:
                    guess[i] = letter
                    g_l += 1
        else:
            print("There is no such letter")
            us_attempt += 1
    if us_attempt == attempts[lvl-1]:    
        print("Game is over. Next time you'll be lucky!\n",
              f"The word was: {gw}")
    else:
        print(gw,"\nGreat job!")
hangman()
    