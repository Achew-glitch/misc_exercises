# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

import random

l_int = [random.randint(-100, 100) for i in range(10)]
print(f'Random list: {l_int}')
print(f'Set of l_int: {set(l_int)}')



non_rep_list = set(l_int)

for el in non_rep_list:
    l_int.remove(el)

print(f'Repeating elements: {l_int}')
for el in set(l_int):
    non_rep_list.remove(el)

print(f'Elements with not have repeat: {non_rep_list}')