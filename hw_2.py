# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1,2 и 3 и т.д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().


users_line = input('Введите несколько цифр через пробел: ')
users_list = users_line.split()
last_i = len(users_list) - 1

for i, val in enumerate(users_list):
    if i % 2 == 0 and i < last_i:
        users_list[i + 1], users_list[i] = users_list[i:i + 2]

print(users_list)
