# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

from sys import exit
import os
import easy

menu = ['Перейти в папку', 'Просмотреть содержимое текущей папки', 'Удалить папку', 'Создать папку']
while True:
    for i in enumerate(menu, 1):
        print(f'{i[0]}. {i[1]}')
    cur_path = os.getcwd()
    print(f'Текущее расположение: {cur_path}')
    print('----------------------')
    answer = input().lower()
    if answer == '1':
        cur_path = os.path.split(cur_path)
        print(cur_path)
        answer = input('В какую директорию перейти: ')
        new_path = os.path.join(os.getcwd(), answer)
        if answer in os.path.split(cur_path[0]):
            os.chdir(cur_path[0])
            print(f'Выполнен переход в директорию {answer}\n{cur_path[0]}')
        elif os.path.exists(new_path):
            os.chdir(new_path)
            print(f'Выполнен переход в директорию {answer}\n{new_path}')
        else:
            print(f'Директория "{answer}" не существует в текущем каталоге')
        print('----------------------')
    elif answer == '2':
        print('Список папок в текущей директории:')
        easy.show_listdir()
        print('----------------------')
    elif answer == '3':
        answer = input('Укажите название директории, которую необходимо удалить: ')
        easy.delete_dir_in_current_path(cur_path, answer)
    elif answer == '4':
        answer = input('Укажите название новой директории: ')
        easy.make_dir_in_curr_path(cur_path, answer)
    elif answer == 'exit':
        exit()
    else:
        print(f'{answer} - такая команда недоступна')
