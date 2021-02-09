# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    ndigits = 10 ** (ndigits + 1)
    result = int(number * ndigits)
    reminder = result % 10
    if reminder >= 5:
        result += 10
    return (result - reminder) / ndigits



print(my_round(2.1234567, 1))
print(my_round(2.1999967, 1))
print(my_round(2.9999967, 3))

