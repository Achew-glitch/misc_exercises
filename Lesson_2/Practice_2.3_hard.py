# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

import random

def check_room (current_room, current_iteration):
    global current_floor
    temp = current_room - n
    cluster = current_iteration ** 2
    if 0 <= temp <= cluster:
        print(f'Current floor: {current_floor}')
        print(f'Rooms: {r}')
        print(f'Temp: {temp}')
        print(f'Current iteration {current_iteration} is legitimate')
        for i in range(current_iteration):
            if temp >= current_iteration:
                temp -= current_iteration
                current_floor -= 1
            else:
                print(f'Current position at floor: {current_iteration - temp}')
                print(f'We found floor: {current_floor}')
                return True


    else:
        print('Next iteration')

n = 12
print(f'n = {n}')
rooms = []
current_room = 0
current_floor = 0
i = 1
while True:

    current_floor += i
    r = i ** 2
    current_room += r
    print(f'Current room: {current_room}')

    if check_room(current_room, i):
        break
    i +=1
