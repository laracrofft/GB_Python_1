# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой


class MyError(Exception):
    txt = 'Вы ввели ноль. Деление на ноль не возможно'

    def __str__(self):
        return self.txt


class Func:
    def __init__(self, arg_1, arg_2):
        self.arg_1 = arg_1
        self.arg_2 = arg_2

    def my_func(arg_1, arg_2):
        if arg_2 == 0:
            raise MyError
        else:
            return arg_1 / arg_2


users_arg1 = int(input('Введите делимое: '))
users_arg2 = int(input('Введите делитель: '))

try:
    print(Func.my_func(users_arg1, users_arg2))
except MyError as err:
    print(err)
else:
    print('Получилось!')
