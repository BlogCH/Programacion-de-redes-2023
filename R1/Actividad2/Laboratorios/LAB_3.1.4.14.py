'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: LAB 3.1.4.13
'''
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y

    def getx(self):
        return self._x

    def gety(self):
        return self._y

    def distance_from_xy(self, x, y):
        return math.hypot(self._x - x, self._y - y)

    def distance_from_point(self, point):
        return math.hypot(self._x - point.getx(), self._y - point.gety())

# Crear instancias de la clase Point
point1 = Point(0, 0)
point2 = Point(1, 1)

# Calcular distancias e imprimir resultados
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
