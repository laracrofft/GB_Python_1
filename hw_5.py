# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
# результат вычисления произведения всех элементов списка

from functools import reduce

result_list = [el for el in range(100, 1000) if el % 2 == 0]


def red_func(el_1, el_2):
    return el_1 * el_2


print(reduce(red_func, result_list))
