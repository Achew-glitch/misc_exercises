# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!


a1 = int(input('Введите число а1: '))
a2 = int(input('Введите число а2: '))

print(f'a1 = {a1}')
print(f'a2 = {a2}')

a1 += a2
a2 = a1 - a2
a1 -= a2

print(f'a1 = {a1}')
print(f'a2 = {a2}')