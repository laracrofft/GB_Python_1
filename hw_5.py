# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран


from random import randint

my_numbers = [randint(1, 20) for i in range(20)]
result = 0
print(my_numbers)

with open('hw_5.txt', 'x', encoding='utf-8') as f:
    for i in my_numbers:
        f.write(f'{i} ')

with open('hw_5.txt', 'r', encoding='utf-8') as f:
    numbers = f.read()
    print(numbers)
    result += sum([int(el) for el in numbers.split()])
    print(result)
