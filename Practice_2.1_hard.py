# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

import re

match = re.search(r'\S = (?P<a>\D\d+)\D \+ (?P<b>\d+.\d+)', equation)
print(f"y = {x * float(match.group('a')) + float(match.group('b'))}")

