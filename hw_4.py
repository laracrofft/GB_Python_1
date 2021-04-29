# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции


user_number = int(input('Введите целое положительное число: '))
result = 0

while user_number > 10:
    s_num = user_number % 10
    user_number //= 10
    if s_num > result:
        result = s_num
print(result)
