# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '12.01.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'


import re

match = re.search('(?P<day>\d{2})\.(?P<month>\d{2})\.(?P<year>\d{4})', date)
try:
    if 31 < int(match.group('day')) or 1 > int(match.group('day')):
        print('Wrong day')
    elif 12 < int(match.group('month')) or 1 > int(match.group('month')):
        print('Wrong month')
    elif 9999 < int(match.group('year')) or 1 > int(match.group('year')):
        print('Wrong year')
    else:
        print(f'Date {".".join(match.groups())} is correct')
except AttributeError:
    print('Wrong lenght of date')
