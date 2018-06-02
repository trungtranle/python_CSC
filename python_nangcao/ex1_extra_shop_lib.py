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
    def __init__(self, ngaydat, trangthai, xuathoadon, list_chitiet):
        self.ngaydat = ngaydat
        self.trangthai = trangthai
        self.xuathoadon = xuathoadon
        self.list_chitiet = list_chitiet
        if self.xuathoadon:
            self.thue = 10/100
        else:
            self.thue = 0

    def tinh_tong_tien(self):
        tong_tien = 0
        for item in self.list_chitiet:
            tong_tien += item.tinh_thanh_tien()
        return tong_tien



class The(object):
    def __init__(self, maso, phuongthuc):
        self.maso = maso
        self.phuongthuc = phuongthuc


class TheATM(The):
    def __init__(self, maso, phuongthuc, sotiencon):
        The.__init__(self, maso, phuongthuc)
        self.sotiencon = sotiencon
        self.loaithe = 'Thẻ ATM'


class TheTinDung(The):
    def __init__(self, maso, phuongthuc, loai, ngayhethan, no_toida):
        The.__init__(self, maso, phuongthuc)
        self.loai = loai
        self.ngayhethan = ngayhethan
        self.no_toida = no_toida
        self.loaithe= 'Thẻ Tín dụng'
    

class ThanhToan(KhachHang, Donhang, The):
    def __init__ (self, CMND, ten, email, dienthoai, diachi, ngaydat, trangthai, xuathoadon, list_chitiet, maso, phuongthuc):
        KhachHang.__init__(self, CMND, ten, email, dienthoai, diachi)
        Donhang.__init__(self, ngaydat, trangthai, xuathoadon, list_chitiet)
        The.__init__(self, maso, phuongthuc)
        self.tong_tien = Donhang.tinh_tong_tien(self)
    
    def in_thanh_toan(self):
        print('===== Đơn hàng ====')
        print('Tên:', self.ten, 'CMND:' , self.CMND, 'Email:', self.email, 'Điện thoại:',self.dienthoai, 'Địa chỉ:', self.diachi)
        print('Ngày đặt:', self.ngaydat)
        if self.trangthai == 1:
            trang_thai = 'Vừa mới đặt'
        elif self.trangthai == 2:
            trang_thai = 'Đã thanh toán'
        elif self.trangthai == 3:
            trang_thai = 'Đã nhận hàng'
        print('Trạng thái:', trang_thai)
        if self.xuathoadon:
            print('Có xuất hóa đơn')
        else:
            print('Không xuất hóa đơn')
        tong = 0
        print('--- Chi tiết ---')
        for item in self.list_chitiet:
            print(item.ten,' - Đơn giá:', item.dongia, '- Số lượng:', item.soluong, '- Thành tiền:', item.tinh_thanh_tien())
            tong += item.tinh_thanh_tien()
        print('Tổng:', tong)
        print('Thẻ thanh toán:', self.maso)
        print('Phương thức:', self.phuongthuc)
