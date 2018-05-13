import math


def la_tam_giac(a, b, c):

    if a + b > c and b + c > a and a + c > b:
        triangle = True
        print('Là tam giác')
    else:
        triangle = False
        print('Không là tam giác')
    return triangle


def tinh_dien_tich(a, b, c):
    p = (a + b + c)/2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area


def tinh_chieu_cao(dien_tich, canh):
    h = 2 * dien_tich / canh
    return h
