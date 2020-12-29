# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4


import  math

def quadratic_equation(a, b, c):
        disc = b ** 2 -  4 * a * c
        if disc > 0:
            x1 = (-b + math.sqrt(disc)) / 2 * a
            x2 = (-b - math.sqrt(disc)) / 2 * a
            return x1, x2
        elif disc < 0:
            print('Решений нет')
        elif disc == 0:
            x1 = x2 = b / 2 * a
            return x1, x2

a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
print(f'Корни уровнения: {quadratic_equation(a, b, c)}')