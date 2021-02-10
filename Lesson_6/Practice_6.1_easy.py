# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt


class Triangle:
    def __init__(self, *args):
        self.vertex = args[0:3]

    def __str__(self):
        return f'Vertex 1: {self.vertex[0]}\n' \
               f'Vertex 2: {self.vertex[1]}\n' \
               f'Vertex 3: {self.vertex[2]}'

    def square(self):
        self.side1 = Triangle.len_side(self.vertex[0], self.vertex[1])
        self.side2 = Triangle.len_side(self.vertex[1], self.vertex[2])
        self.side3 = Triangle.len_side(self.vertex[0], self.vertex[2])



    @property
    def len_side(v1, v2):
        s1 = v2[0] - v1[0]
        s2 = v2[1] - v1[1]
        return sqrt(pow(s1, 2) + pow(s2, 2))




vertex1 = (1, 2)
vertex2 = (3, 5)
vertex3 = (5, 2)
figure1 = Triangle(vertex1, vertex2, vertex3)
print(figure1)
