# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов


def my_func(arg_1, arg_2, arg_3):
    """Создает список принимаемых аргументов numbers_list
    Выбирает среди них наибольший, удаляет его из списка numbers_list
    Добавляет наибольшее значение в итоговый список result,
    Повторяет с оставшимися аргументами и суммирует результат
    """
    numbers_list = [arg_1, arg_2, arg_3]
    result = []
    num_1 = max(numbers_list)
    result.append(num_1)
    numbers_list.remove(num_1)
    num_2 = max(numbers_list)
    result.append(num_2)
    numbers_list.remove(num_2)
    print(sum(result))


my_func(10, 7, 0)
