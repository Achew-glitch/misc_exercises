# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

import re


class UppercaseFraction:
    def __init__(self):
        regex = r' *(?P<integer>-?\d*) +(?P<numerator>\d*) */ *(?P<denominator>\d*) *'
        self.match = re.search(regex, input('Введите дробь: '))

    def __str__(self):
        return f'{self.match.group("integer")} {self.match.group("numerator")}/{self.match.group("denominator")}'

    def __add__(self, other):
        sum_int = int(self.match.group('integer')) + int(other.match.group('integer'))
        sum_num = int(self.match.group('numerator')) * int(other.match.group('denominator')) + \
                  int(other.match.group('numerator')) * int(self.match.group('denominator'))
        sum_denom = int(self.match.group('denominator')) * int(other.match.group('denominator'))
        if sum_num // sum_denom == 1:
            sum_int += 1
            sum_num -= sum_denom
        else:
            print('Некорректная запись дроби')
        return f'{sum_int} {sum_num}/{sum_denom}'

    def __sub__(self, other):
        sub_int = int(self.match.group('integer')) - int(other.match.group('integer'))
        sub_num = int(self.match.group('numerator')) * int(other.match.group('denominator')) - \
                  int(other.match.group('numerator')) * int(self.match.group('denominator'))
        sub_denom = int(self.match.group('denominator')) * int(other.match.group('denominator'))
        if sub_int > 0 and sub_num < 0:
            sub_int -= 1
            sub_num += sub_denom
        elif sub_int < 0 and sub_num > 0:
            sub_int += 1
            sub_num -= sub_denom
        elif sub_int < 0 and sub_num < 0:
            sub_num = -(sub_num)
        else:
            print('Некорректная запись дроби')
        return f'{sub_int} {sub_num}/{sub_denom}'


fr_1 = UppercaseFraction()
fr_2 = UppercaseFraction()

print(f'Результат сложения: {fr_1 + fr_2}')
print(f'Результат вычитания: {fr_1 - fr_2}')