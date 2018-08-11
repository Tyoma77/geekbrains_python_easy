import math
import lesson3.hw03_normal as l3


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определть методы позволяющие вычислить: Площадь, высоту и периметр фигуры

# Задача-2: Написать Класс Равнобочная трапеция, заданной координатами 4-х точек.
#  Предусмотреть в классе методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления: длины сторон, периметр, площадь.


class Triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def area(self):
        return math.sqrt((Triangle.perimeter() / 2) * (Triangle.perimeter() / 2 - l3.get_length(self.x, self.y)) *
                         (Triangle.perimeter() / 2 - l3.get_length(self.x, self.z)) * (Triangle.perimeter() / 2 -
                                                                                       l3.get_length(self.z, self.y)))

    def height(self):
        return 2 * Triangle.height() / l3.get_length(self.x, self.y)

    def perimeter(self):
        return l3.get_length(self.x, self.y) + l3.get_length(self.x, self.z) + l3.get_length(self.z, self.y)


class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def isosceles(self):
        return Trapeze.get_length_line(self.a, self.b) == Trapeze.get_length_line(self.c, self.d)

    def get_length_line(self, x, y):
        return math.sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2)

    def perimeter(self):
        return Trapeze.get_length_line(self.a, self.b) + Trapeze.get_length_line(self.a, self.d) + \
               Trapeze.get_length_line(self.b, self.c) + Trapeze.get_length_line(self.c, self.d)

    def height(self):
        p = (Trapeze.get_length_line(self.a, self.b) + Trapeze.get_length_line(self.c, self.d) +
             Trapeze.get_length_line(self.a, self.d) - Trapeze.get_length_line(self.b, self.c)) / 2
        s = math.sqrt(p * (p - Trapeze.get_length_line(self.a, self.b)) * (p - Trapeze.get_length_line(self.c, self.d))
                      * (p - (Trapeze.get_length_line(self.a, self.d) - Trapeze.get_length_line(self.b, self.c))))
        return 2 * s / (Trapeze.get_length_line(self.a, self.d) - Trapeze.get_length_line(self.b, self.c))

    def area(self):
        return (Trapeze.get_length_line(self.a, self.d) + Trapeze.get_length_line(self.b, self.c)) * \
               Trapeze.height() / 2
