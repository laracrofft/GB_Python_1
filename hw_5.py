# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них


my_list = [7, 5, 3, 3, 2]

users_number = int(input('Введите любое натуральное число: '))

for el in my_list:
    max_number = max(my_list)
    if users_number > max_number:
        my_list.insert(0, users_number)
    elif users_number in my_list:
        list_number = my_list.index(users_number)
        my_list.insert(list_number, users_number)
    elif users_number not in my_list:
        list_number = my_list.index(users_number - 1)
        my_list.insert(list_number, users_number)
    else:
        my_list.append(users_number)
    print(my_list)
    break
