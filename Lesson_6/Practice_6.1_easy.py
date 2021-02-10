# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt


class Triangle:
    def __init__(self, *args):
        self.side1 = Triangle.len_side(args[0], args[1])
        self.side2 = Triangle.len_side(args[1], args[2])
        self.side3 = Triangle.len_side(args[0], args[2])

    def sides(self):
        return f'Side 1: {self.side1}\n' \
               f'Side 2: {self.side2}\n' \
               f'Side 3: {self.side3}'

    def __str__(self):
        return f'ABC'

    def square(self):
        return 0.5 * self.side3 * Triangle.height(self)

    def perimeter(self):
        return sum((self.side1, self.side2, self.side3))

    def height(self):
        return sqrt(pow(self.side2, 2) - pow(pow(self.side2, 2) - pow(self.side1, 2) + pow(self.side3, 2), 2) / (
                4 * pow(self.side3, 2)))

    def len_side(v1, v2):
        s1 = v2[0] - v1[0]
        s2 = v2[1] - v1[1]
        return sqrt(pow(s1, 2) + pow(s2, 2))


vertex1 = (1, 2)
vertex2 = (3, 5)
vertex3 = (5, 3)
figure1 = Triangle(vertex1, vertex2, vertex3)
print(f'Треугольник: {figure1}')
print(f'Стороны треугльника {figure1}: {figure1.sides()}')
print(f'Площадь треугольника {figure1}: {figure1.square()}')
print(f'Перимеотр треугольника {figure1}: {figure1.perimeter()}')
print(f'Высота треугольника {figure1}: {figure1.height()}')
