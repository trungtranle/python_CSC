import math


class Diem(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def tinh_khoang_cach(A, B):
    khoang_cach = math.sqrt((A.x - B.x)**2 + (A.y - B.y)**2)
    return khoang_cach


def tinh_dien_tich_hinh_tron(A, B):
    radius = tinh_khoang_cach(A, B)
    area = math.pi * (radius ** 2)
    return area


def tinh_chu_vi_hinh_tron(A, B):
    diameter = tinh_khoang_cach(A, B) * 2
    circumfrence = math.pi * diameter
    return circumfrence


def tinh_chieu(A, B):
    chieu_dai = abs(A.x - B.x)
    chieu_rong = abs(A.y - B.y)
    return chieu_dai, chieu_rong


def tinh_dien_tich_hcn(A, B):
    chieu_dai, chieu_rong = tinh_chieu(A, B)
    area = chieu_dai * chieu_rong
    return area


def tinh_chu_vi_hcn(A, B):
    chieu_dai, chieu_rong = tinh_chieu(A, B)
    perimeter = (chieu_dai + chieu_rong) * 2
    return perimeter