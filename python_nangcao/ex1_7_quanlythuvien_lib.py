class Sach(object):
    def __init__(self, masach, tensach, ngaynhap, dongia, soluong, nxb):
        self.masach = masach
        self.tensach = tensach
        self.ngaynhap = ngaynhap
        self.dongia = dongia
        self.soluong = soluong
        self.nxb = nxb

    def tinh_thanh_tien(self):
        thanh_tien = self.soluong * self.dongia
        return thanh_tien

    def in_sach(self):
        print(self.masach, '-', self.tensach, '-', self.ngaynhap, '-', self.dongia, '-', self.soluong, '-', self.nxb, '- Thành tiền', self.tinh_thanh_tien())

class Sachgiaokhoa(Sach):
    moi_count = 0
    cu_count = 0
    def __init__(self, masach, tensach, ngaynhap, dongia, soluong, nxb, tinhtrang):
        Sach.__init__(self, masach, tensach, ngaynhap, dongia, soluong, nxb)
        self.tinhtrang = tinhtrang
        assert (self.tinhtrang == 1 or self.tinhtrang ==
                0), "Tình trạng sách không đúng"
        if self.tinhtrang == 1: 
            Sachgiaokhoa.moi_count += 1
        else:
            Sachgiaokhoa.cu_count += 1

    def tinh_thanh_tien(self):
        if self.tinhtrang == 1:
            thanh_tien = Sach.tinh_thanh_tien(self)
        else:
            thanh_tien = Sach.tinh_thanh_tien(self) * 0.5
        return thanh_tien

    def in_sach(self):
        Sach.in_sach(self)
        print('Sách mới: ', Sachgiaokhoa.moi_count)
        print('Sách cũ:', Sachgiaokhoa.cu_count)


class Sachthamkhao(Sach):
    def __init__(self, masach, tensach, ngaynhap, dongia, soluong, nxb, thue):
        Sach.__init__(self, masach, tensach, ngaynhap, dongia, soluong, nxb)
        self.thue = thue

    def tinh_thanh_tien(self):
        thanh_tien = Sach.tinh_thanh_tien(self) + Sach.tinh_thanh_tien(self) * self.thue/100
        return thanh_tien
