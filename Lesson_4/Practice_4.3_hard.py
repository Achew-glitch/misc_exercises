# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

from random import randint
data_input = []
for i in range(8):
    data_input.append([randint(1,8), randint(1,8)])

print(data_input)

for figure in data_input:
    i = data_input.index(figure) + 1
    print(f'-------------------\nfigure 1: {figure}\ni = {i}')
    x_1 = figure[0]
    y_1 = figure[1]
    while i < len(data_input):
        print(f'figure 2: {data_input[i]}')
        x_2 = data_input[i][0]
        y_2 = data_input[i][1]
        if x_1 == x_2 or y_1 == y_2 or x_1 - x_2 == y_1 - y_2:
            print('YES')
        else:
            print('NO')
        i += 1