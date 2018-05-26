from ex1_5_tinhluong_lib import Nhanvien

class NhanVienKinhDoanh (Nhanvien):
    def __init__(self, hoten, heso, songuoi, phucap, doanhso):
        Nhanvien.__init__(self, hoten, heso, songuoi, phucap)
        self.doanhso = doanhso
    
    def tinh_luong_thuong(self):
        luong_thuong = Nhanvien.canban * self.doanhso
        return luong_thuong
    
    def tinh_thu_nhap(self):
        thu_nhap = Nhanvien.tinh_thu_nhap(self) + NhanVienKinhDoanh.tinh_luong_thuong(self)
        return thu_nhap
    
class NhanVienSanXuat (Nhanvien):
    dinh_muc = 450 
    don_gia = 10000
    def __init__ (self, hoten, heso, songuoi, phucap, sosanpham):
        Nhanvien.__init__ (self, hoten, heso, songuoi, phucap)
        self.sosanpham = sosanpham
    
    def tinh_luong_thuong(self):
        if self.sosanpham > NhanVienSanXuat.dinh_muc:
            luong_thuong = (self.sosanpham - NhanVienSanXuat.dinh_muc) * NhanVienSanXuat.don_gia
        else:
            luong_thuong = 0
        return luong_thuong

    def tinh_thu_nhap(self):
        thu_nhap = Nhanvien.tinh_thu_nhap(self) + NhanVienSanXuat.tinh_luong_thuong(self)
        return thu_nhap   