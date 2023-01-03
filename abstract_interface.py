import math
from abc import abstractmethod


class Shape:

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_shape_details(self):
        pass

class Circle(Shape):

    def get_shape_details(self):
        return {
            "radius" : self.radius
        }

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pow(self.radius, 2) * math.pi


class Triangle(Shape):

    def __init__(self, length, base):
        self.base = base
        self.length = length

    def get_area(self):
        return self.length * self.base * 0.5


shape = Shape()
print(shape.get_area())
circle = Circle(5)
print(circle.get_area())
triangle = Triangle(10, 5)
print(triangle.get_area())
print(circle.get_shape_details())
