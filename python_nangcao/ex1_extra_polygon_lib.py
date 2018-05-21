import math


class Polygon(object):
    def __init__(self, sides):
        self.side = sides
        self.sides_mesurement = []
        for i in range(sides):
            self.sides_mesurement.append(0)

    def input_side(self):
        for i in range(0, len(self.sides_mesurement)):
            self.sides_mesurement[i] = eval(
                input('Nhập độ dài cạnh %d: ' % (i+1)))

    def print_mesurement(self):
        for i in range(0, len(self.sides_mesurement)):
            print('Độ dài cạnh thứ', i + 1, "=", self.sides_mesurement[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, sides = 3)

    def print_mesurement(self):
        print('Tam giác có ba cạnh')
        Polygon.print_mesurement(self)

    def calculate_perimeter(self):
        a, b, c = self.sides_mesurement
        p = a + b + c
        return p

    def calculate_area(self):
        a, b, c = self.sides_mesurement
        q = Triangle.calculate_perimeter(self) / 2
        s = math.sqrt(q * (q - a) * (q - b) * (q - c))
        return s
