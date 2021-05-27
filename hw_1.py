# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных

class Data:
    def __init__(self, ddmmyy):
        self.ddmmyy = str(ddmmyy)

    @classmethod
    def extract(cls, ddmmyy):
        my_date = []

        for i in ddmmyy.split():
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(dd, mm, yy):

        if 1 <= dd <= 31:
            if 1 <= mm <= 12:
                if 2021 >= yy >= 0:
                    return 'Все верно'
                else:
                    return 'Введен не верный год'
            else:
                return 'Введен не верный месяц'
        else:
            return 'Введен не верный день'


print(Data.extract('01 - 12 - 2014'))
print(Data.valid(1, 4, 2022))
print(Data.valid(11, 13, 2011))
print(Data.valid(1, 11, 2000))
