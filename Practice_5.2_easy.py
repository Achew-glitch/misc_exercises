# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

print(os.listdir(path=os.getcwd()))
for dir in os.listdir(path=os.getcwd()):
    if os.path.isdir(dir):
        print(f'{dir}')
