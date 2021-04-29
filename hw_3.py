# Узнайте у пользователя число n.
# Найдите сумму чисел n+nn+nnn. Например,пользователь ввел число 3. Считаем 3 + 33 + 333 =369


user_n = (input('Введите число от 1 до 9: '))

double_n = int(user_n + user_n)
triple_n = int(user_n + user_n + user_n)

result = int(user_n) + double_n + triple_n
print(result)
