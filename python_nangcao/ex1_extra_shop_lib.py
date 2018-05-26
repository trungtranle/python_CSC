class KhachHang(object):
    def __init__(self, CMND, ten, email, dienthoai, diachi):
        self.CMND = CMND 
        self.ten = ten
        self.email = email
        self.dienthoai = dienthoai
        self.diachi = diachi

class Chitiet(object):
    def __init__(self, ten, soluong, dongia):
        self.ten = ten
        self.soluong = soluong
        self.dongia = dongia
    def tinh_thanh_tien(self):
        thanhtien = self.soluong * self.dongia
        return thanhtien

class Donhang(object):
    def __init__(self, ngaydat, trangthai, xuathoadon):
        self.ngaydat = ngaydat
        self.trangthai = trangthai
        self.xuathoadon = xuathoadon
        if self.xuathoadon == True:
            self.thue = 10/100
        else:
            self.thue = 0

class The(object):
    def __init__(self, maso, phuongthuc):
        self.maso = maso
        self.phuongthuc = phuongthuc

class TheATM(The):
    def __init__(self, maso, phuongthuc, sotiencon):
        The.__init__(maso, phuongthuc)
        self.sotiencon = sotiencon

class TheTinDung(The):
    def __init__(self, maso, phuongthuc, loai, ngayhethan, no_toida):
        The.__init__(maso, phuongthuc)
        self.loai = loai
        self.ngayhethan = ngayhethan
        self.no_toida = no_toida