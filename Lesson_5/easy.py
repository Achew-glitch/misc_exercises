import os
from shutil import rmtree

def show_listdir():
    for dir in os.listdir(path=os.getcwd()):
        if os.path.isdir(dir):
            print(f'{dir}')


def make_dir_in_curr_path(cur_path, answer):
    try:
        os.mkdir(os.path.join(cur_path, f'{answer}'))
        print(f'Директория {answer} успешно создана')
    except FileExistsError:
        print(f'{answer} - такая директория уже существует')


def delete_dir_in_current_path(cur_path, answer):
    try:
        rmtree(os.path.join(cur_path, f'{answer}'))
        print(f'Директория {answer} успешно удалена')
    except FileNotFoundError:
        print('Такой директории не существует')