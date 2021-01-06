# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def parallelogram(arg_1, arg_2, arg_3, arg_4):
    if arg_1[0] - arg_3[0] == arg_2[0] - arg_4[0] and \
            arg_1[1] - arg_2[1] == arg_3[1] - arg_4[1]:
        print('It is parallelogram')
    else:
        print('It is not parallelogram')


a1 = [1, 2]
a2 = [5, 2]
a3 = [2, -4]
a4 = [6, -4]
parallelogram(a1, a2, a3, a4)

b1 = [1, 2]
b2 = [2, 2]
b3 = [1, 2]
b4 = [6, 2]
parallelogram(b1, b2, b3, b4)