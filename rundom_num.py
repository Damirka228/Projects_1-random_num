import random
num_random = random.randint(0, 5)
num_user = int(input("Введите число: "))
x = 1
while x >= 0:
    x += 1
    if num_user == num_random:
        accept = "Вы угадали число"
        print(accept)
        break
    else:
        not_accepted = "Вы не угадали число"
        print(not_accepted)
        b = int(input())
        if b == num_random:
            print("Вы угадали число", "c", x, "попытки")
            break