# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

from random import randint

rand_list = [randint(-100, 100) for i in range(10)]
print(f'rand_list: {rand_list}')

sort_list = [sort_el for sort_el in rand_list
             if sort_el % 3 == 0 and sort_el > 0 and sort_el % 4 != 0]
print(f'sort_list: {sort_list}')