# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count, cycle

for el in count(22):
    if el > 33:
        break
    else:
        print(el)


z = 0
for el in cycle("КУКУ"):
    if z > 11:
        break
    print(el)
    z += 1

