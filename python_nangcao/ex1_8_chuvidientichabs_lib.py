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
        
