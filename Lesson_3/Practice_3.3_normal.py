# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter(func, arg):
    result = []
    for el in arg:
        result.append(func(el))
    return iter(result)


def upper_case(s):
    return s.upper()


s = ['lower character string', 'another lower string', 'last string']
for el in s:
    print(el)

for el in filter(upper_case, s):
    print(el)
