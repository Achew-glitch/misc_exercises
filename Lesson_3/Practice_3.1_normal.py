# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    cur = 1
    prev = 1
    i = 2
    while i < m:
        result = cur + prev
        prev = cur
        cur = result
        i += 1
        if i >= n:
            yield result


def matrix_mul(a, b):
    return [[
        a[0][0] * b[0][0] + a[0][1] * b[1][0],
        a[0][0] * b[0][1] + a[0][1] * b[1][1]
    ], [
        a[1][0] * b[0][0] + a[1][1] * b[1][0],
        a[1][0] * b[0][1] + a[1][1] * b[1][1]
    ]]


def pow(p):
    m = [[1, 1], [1, 0]]
    t = [[1, 0], [0, 1]]
    while p:
        if p % 2:
            t = matrix_mul(t, m)
        m = matrix_mul(m, m)
        p //= 2
    return t


def fib(n):
    return pow(n)[1][0]

print(fib(3))

