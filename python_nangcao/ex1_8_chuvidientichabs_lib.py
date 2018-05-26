import abc
import math


class Shape(object):
    __metaclass__ = abc.ABCMeta

    @classmethod
    @abc.abstractclassmethod
    def cal_area(self):
        pass

    def cal_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def cal_area(self):
        area = math.pi * self.r ** 2
        return area

    def cal_perimeter(self):
        perimeter = math.pi * self.r * 2
        return perimeter


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def cal_perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        return perimeter

    def cal_area(self):
        q = Triangle.cal_perimeter(self) / 2
        area = math.sqrt(q*(q-self.side1)*(q-self.side2)*(q-self.side3))
        return area


class Rectangle(Shape):
    def __init__(self, length, wide):
        self.length = length
        self.wide = wide

    def cal_area(self):
        area = self.length * self. wide
        return area

    def cal_perimeter(self):
        perimeter = 2 * (self.length + self.wide)
        return perimeter
