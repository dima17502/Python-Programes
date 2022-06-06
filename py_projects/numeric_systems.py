
def translate_num(n, new_base):
    res = ""
    numbers = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    while n > 0:
        res += str(numbers[n % new_base])
        n //= new_base
    return res[::-1]





def main():
    print("Enter the number in decimal system: ")
    n = int(input())
    print("Enter base you want to switch: ")
    new_base = int(input())
    print(translate_num(n, new_base))

main()