import math


class Tamgiac(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tinh_chu_vi(self):
        p = (self.a + self.b + self.c)/2
        return p

    def tinh_dien_tich(self):
        p = self.tinh_chu_vi()
        area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return area
    '''
    def tinh_chieu_cao(self, self.tinh_dien_tich()):
        h = 2 * dien_tich / canh
        return h
    '''
    def in_ket_qua(self):
        ketqua = ''
        ketqua += 'Tam giác có ba cạnh '  + str(self.a) + ',' + str(self.b) + ',' +str(self.c)
        ketqua += '\n' + 'Chu vi = ' + str(self.tinh_chu_vi())
        ketqua += '\n' + 'Diện tích ' + str(self.tinh_dien_tich())
        return ketqua


def la_tam_giac(a, b, c):
    return a + b > c and a + c > b and b + c > a