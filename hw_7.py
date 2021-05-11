# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом:for el in fact(n). Функция отвечает за получение
# факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!

from math import factorial


def my_gen(number):
    count = 1
    while count <= number:
        yield factorial(count)
        count += 1


my_numbers = []
for el in my_gen(5):
    my_numbers.append(el)

print(my_numbers)
