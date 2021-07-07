
__author__='Алферьев Дмитрий Александрович'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle:
    def __init__(self, A, B, C):
        # Функция для нахождения длины стороны в соответствии с имеющимися данными о координатах.
        def sideLen(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)
        self.A = A
        self.B = B
        self.C = C
        # Поиск длины сторон.
        self.AB = sideLen(self.A, self.B)
        self.BC = sideLen(self.B, self.C)
        self.CA = sideLen(self.C, self.A)
 
    # Вычисление площади треугольника по формуле Герона.
    def areaTriangle(self):
        semi_perimeter = self.perimeterTriangle() / 2
        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.AB)
                         * (semi_perimeter - self.BC)
                         * (semi_perimeter - self.CA))
 
    # Вычисление периметра треугольника.
    def perimeterTriangle(self):
        return self.AB + self.BC + self.CA
 
    # Вычисление высоты треугольника.
    def heightTriangle(self):
        return self.areaTriangle() / (self.AB / 2)
 
### Параметры координат для треугольника по которому проведем расчеты. ###
treugolnik = Triangle((1, 1), (5, 5), (6, 1))
 
print('Площадь заданного треугольника:', treugolnik.areaTriangle())
print('Периметр заданного треугольника:', treugolnik.heightTriangle())
print('Высота заданного треугольника:', treugolnik.perimeterTriangle())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, A, B, C, D):
        # Функция вычисляет длину стороны согласно координатам точек
        def sideLen(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)
 
        def areaTriangle(len1, len2, len3):
            semi_perimeter = (len1 + len2 + len3) / 2
 
            return math.sqrt(semi_perimeter
                             * (semi_perimeter - len1)
                             * (semi_perimeter - len2)
                             * (semi_perimeter - len3))
 
        self.A = A
        self.B = B
        self.C = C
        self.D = D
 
        self.AB = sideLen(self.A, self.B)
        self.BC = sideLen(self.B, self.C)
        self.CD = sideLen(self.C, self.D)
        self.DA = sideLen(self.D, self.A)
        self.diagonal_AC = sideLen(self.C, self.A)
        self.diagonal_BD = sideLen(self.B, self.D)
        self.perimeter = self.AB + self.BC + self.CD + self.DA
 
        # представим трапецию как 2 треугольника и сложим 2 площади этих треугольников
        # Для этого у нас есть все необходимые длины сторон
        self.area = areaTriangle(self.AB, self.diagonal_BD, self.DA) \
                    + areaTriangle(self.diagonal_BD, self.BC, self.CD)
 
    def isTrapezeEqu(self):
        if self.diagonal_AC == self.diagonal_BD:
            return True
        return False

### Параметры координат для трапеции по которой проведем расчеты. ###
trapezium = Trapeze((1, 1), (6, 1), (2, 3), (5, 3))
 
print('Проверка на то - является заданная трапеция равнобочной или нет?:', trapezium.isTrapezeEqu())
print('Длина сторон трапеции: {}, {}, {}, {}'.format(trapezium.AB, trapezium.BC, trapezium.CD, trapezium.DA))
print('Периметр трапеции:', trapezium.perimeter)
print('Площадь трапеции:', trapezium.area)
