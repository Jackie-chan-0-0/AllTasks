input_user_n = int(input("Введите значение n: "))
input_user_m = int(input("Введите значение m: "))
i = 1
print("Полученный путь: ", end='')
while True:
    print(i, end='')
    i = 1 + (i + input_user_m - 2) % input_user_n
    if i == 1:
        break