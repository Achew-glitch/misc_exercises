# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import random, math

l_int = []
for i in range(10):
    i = random.randint(1, 100)
    if i % 2 == 0:
        l_int.append(-i)
    else:
        l_int.append(i)

print(f'List of integers: {l_int}')

result_list = []
for i in l_int:
    try:
        i = math.sqrt(i)
        if i - int(i) == 0:
            result_list.append(i)
    except ValueError:
        pass

print(result_list)
