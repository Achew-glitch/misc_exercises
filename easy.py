import os

def show_listdir():
    for dir in os.listdir(path=os.getcwd()):
        if os.path.isdir(dir):
            print(f'{dir}')