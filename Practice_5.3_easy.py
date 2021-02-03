# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
import shutil

name = os.path.basename(__file__)
dir = os.getcwd()
shutil.copyfile(os.path.join(dir, name), os.path.join(dir, f'copy_{name}'))
print(f'Копирование файла {name} успешно завершено')
