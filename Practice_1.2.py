# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a1 = int(input('Введите число а1: '))
a2 = int(input('Введите число а2: '))

print(f'a1 = {a1}')
print(f'a2 = {a2}')

a1, a2 = a2, a1

print(f'a1 = {a1}')
print(f'a2 = {a2}')