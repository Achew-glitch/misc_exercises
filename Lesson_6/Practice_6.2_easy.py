# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
from math import sqrt


class Isosceles_Trapezoid:
    def __init__(self, *args):
        if Isosceles_Trapezoid.len_side(args[0], args[2]) \
                == Isosceles_Trapezoid.len_side(args[3], args[1]):
            self.side1 = Isosceles_Trapezoid.len_side(args[0], args[1])
            self.side2 = Isosceles_Trapezoid.len_side(args[1], args[2])
            self.side3 = Isosceles_Trapezoid.len_side(args[2], args[3])
            self.side4 = Isosceles_Trapezoid.len_side(args[0], args[3])
        else:
            raise Exception('Трапеция не равнобедренная\nПроверьте указанные координаты')

    def __str__(self):
        return f'Сторона 1: {self.side1}\n' \
               f'Сторона 2: {self.side2}\n' \
               f'Сторона 3: {self.side3}\n' \
               f'Сторона 4: {self.side4}'

    def len_side(v1, v2):
        s1 = v2[0] - v1[0]
        s2 = v2[1] - v1[1]
        return sqrt(pow(s1, 2) + pow(s2, 2))

    def perimeter(self):
        return sum((self.side1, self.side2, self.side3, self.side4))

    def square(self):
        if self.side1 == self.side3:
            return (self.side4 + self.side2) / 4 * \
                   sqrt(4 * pow(self.side1, 2) - pow(self.side4 - self.side2, 2))
        else:
            return (self.side1 + self.side3) / 4 * \
                   sqrt(4 * pow(self.side2, 2) - pow(self.side1 - self.side3, 2))


vertex1 = (1, 1)
vertex2 = (1, 6)
vertex3 = (4, 5)
vertex4 = (4, 2)
abcd = Isosceles_Trapezoid(vertex1, vertex2, vertex3, vertex4)
print(abcd)
print(f'Периметр: {abcd.perimeter()}')
print(f'Площадь: {abcd.square()}')
