# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

from random import randint
import re

with open('random_integers.txt', 'w', encoding='utf-8') as w:
    for r_int in range(1, 2501):
        w.write(str(randint(0,9)))
result = []
with open('random_integers.txt', encoding='utf-8') as r:
    read = r.readline()
    for i in range(0,10):
        regex = f'{i}+'
        match = re.findall(regex, read)
        result.append(sorted(match, reverse=True)[0])
print(sorted(result, key=lambda result: len(result), reverse=True)[0])
