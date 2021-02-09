# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
from shutil import rmtree


def make_dir_in_curr_path():
    current_dir = os.getcwd()
    try:
        for i in range(1, 10):
            os.mkdir(os.path.join(current_dir, f'dir_{i}'))
    except FileExistsError:
        print('Такая директория уже существует')


def delete_dir_in_current_path():
    current_dir = os.getcwd()
    try:
        for i in range(1, 10):
            rmtree(os.path.join(current_dir, f'dir_{i}'))
    except FileNotFoundError:
        print('Такой директории не существует')


while True:
    answer = input('Создать или удалить папки?\n').lower()
    if answer == 'создать':
        make_dir_in_curr_path()
        print('Готово')
    elif answer == 'удалить':
        delete_dir_in_current_path()
        print('Готово')
    elif answer == 'выход':
        break
    else:
        print(f'{answer} - такоей операции не могу выполнить')
