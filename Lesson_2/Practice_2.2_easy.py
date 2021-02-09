# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [2, 3, 2, 3, 4]

print(f'List_1: {list_1}')
print(f'Delete list: {set(list_2)}')
for d_el in set(list_2):
    print(f'Delete element: {d_el}')
    list_1.remove(d_el)
print(f'Result list: {list_1}')
