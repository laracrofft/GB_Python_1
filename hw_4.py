# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл

dictionary = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

result = []

with open('text_4.txt', 'r', encoding='utf-8') as f:
    for line in f:
        numbers = line.split(' - ')
        if numbers[0] in dictionary:
            nomer = dictionary[numbers[0]]
            result.append(nomer + ' - ' + numbers[1])

print(result)

new_f = open('text_4_1.txt', 'x')
new_f.writelines(result)
new_f.close()
