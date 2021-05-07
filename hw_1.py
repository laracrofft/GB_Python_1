# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль


def my_func(arg_1, arg_2):
    """Осуществляет деление первого аргумента на второй"""
    return arg_1 / arg_2


users_arg1 = int(input('Введите делимое: '))
users_arg2 = int(input('Введите делитель: '))

try:
    print(my_func(users_arg1, users_arg2))
except ZeroDivisionError:
    print('Деление на ноль не возможно')

