ID_user_VK = input("Введите id пользователя:")

while True:
    if ID_user_VK.isdigit() == False:
        print("Ошибка! Введите корректный id")
        ID_user_VK = input("Введите id пользователя:")
    else:
        break

print(ID_user_VK)
