# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
from shutil import copyfile

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


def make_dir():
    if not name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(name))
    except FileExistsError:
        print('директория {} уже существует'.format(name))


def ping():
    print("pong")


def copy_file():
    if not name:
        print('Необходимо указать имя файла вторым параметром')
        return
    file_name = os.path.join(os.getcwd(), name)
    print(os.getcwd())
    try:
        copyfile(file_name, os.path.join(os.getcwd(), f'copy_{name}'))
        print(f'Файл {name} успешно скопирован')
    except FileNotFoundError:
        print(f'{name} - такой файл не существует')


def remove_file():
    if not name:
        print('Необходимо указать имя файла вторым параметром')
        return
    file_name = os.path.join(os.getcwd(), name)
    try:
        os.remove(file_name)
        print(f'Файл {name} успешно удален')
    except FileNotFoundError:
        print(f'{name} - такой файл не существует')


def change_dir():
    if not name:
        print('Необходимо указать необходимый путь вторым параметром')
        return
    try:
        relative_path = os.path.split(os.getcwd())
        new_path = os.path.join(os.getcwd(), name)
        if name.startswith('/') or name.startswith('C') or name.startswith('D'):
            os.chdir(name)
            print(f'Тукщая директория: {os.getcwd()}')
        elif name in relative_path[0]:
            os.chdir(relative_path[0])
            print(f'Текущая директория {os.getcwd()}')
        elif os.path.exists(new_path):
            os.chdir(new_path)
            print(f'Текущая директория: {os.getcwd()}')
        else:
            print(f'{name} - такой директории не существует в текущем каталоге')
    except FileNotFoundError:
        print(f'{name} - такой путь не существует')


def full_path():
    print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": full_path
}

try:
    name = sys.argv[2]
except IndexError:
    name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
