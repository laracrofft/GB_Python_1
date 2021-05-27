# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка


class MyError(Exception):
    txt = 'Вы ввели символ'

    def __str__(self):
        return self.txt


def num_list():
    result = []
    while True:
        un = input('Введите число или stop для завершения: ')
        try:
            if 'stop' in un:
                break
            elif un.isdigit():
                result.append(int(un))
                print(result)
            else:
                raise MyError
        except MyError as e:
            print(e)


num_list()
