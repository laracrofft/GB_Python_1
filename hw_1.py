# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

filename, time, rate, bonus = argv
try:
    result = int(time) * int(rate) + int(bonus)
    print(f'Зарплата сотрудника составляет: {result}')
except ValueError:
    print('Введите число')

