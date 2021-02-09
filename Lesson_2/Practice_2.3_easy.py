# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

import random

r_int = [random.randint(1, 100) for el in range(10)]
print(f'List of integer: {r_int}')
sort_int = []
for el in r_int:
    if el % 2 == 0:
        sort_int.append(el / 4)
    else:
        sort_int.append(el * 2)

print(f'Result list: {sort_int}')