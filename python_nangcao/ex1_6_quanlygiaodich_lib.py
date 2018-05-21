class GiaoDich(object):
    def __init__(self, magiaodich, ngaygiaodich, dongia, soluong, loaigiaodich, loaitien):
        assert(loaigiaodich == 1 or loaigiaodich == 2)
        self.magiaodich = magiaodich
        self.ngaygiaodich = ngaygiaodich
        self.dongia = dongia
        self.soluong = soluong
        self.loaigiaodich = loaigiaodich
        self.loaitien = loaitien

    def tinh_thanh_tien(self):
        thanh_tien = self.soluong * self.dongia
        return thanh_tien

    giao_dich_list = []

    def them_vao_danh_sach(self):
        gd = str(self.magiaodich) + ' - ' + str(self.ngaygiaodich) + ' - ' + self.loaitien + ' - ' + \
            str(self.soluong) + ' - ' + str(self.dongia) + \
            ' - Thành tiền: ' + str(GiaoDich.tinh_thanh_tien(self))
        GiaoDich.giao_dich_list.append(gd)

    def in_giao_dich_cuoi(self):
        print(GiaoDich.giao_dich_list[-1])


class GiaoDichVang(GiaoDich):
    def __init__(self, magiaodich, ngaygiaodich, dongia, soluong, loaigiaodich, loaitien):
        GiaoDich.__init__(self, magiaodich, ngaygiaodich, dongia, soluong, loaigiaodich, loaitien)


class GiaoDichTien(GiaoDich):
    def __init__(self, magiaodich, ngaygiaodich, dongia, soluong, loaigiaodich,  loaitien, muaban):
        GiaoDich.__init__(self, magiaodich, ngaygiaodich, dongia, soluong, loaigiaodich,  loaitien)
        self.muaban = muaban

    def tinh_thanh_tien(self):
        assert(self.muaban == 1 or self.muaban == 0)
        if self.muaban == 1:
            thanh_tien = self.soluong * self.dongia
        else:
            thanh_tien = self.soluong * self.dongia*1.05
        return thanh_tien

    def them_vao_danh_sach(self):
        if self.muaban == 1:
            gd = 'Giao dịch mua ' + str(self.magiaodich) + ' - ' + str(self.ngaygiaodich) + ' - ' + self.loaitien + ' - ' + \
            str(self.soluong) + ' - ' + str(self.dongia) + \
            ' - Thành tiền: ' + str(GiaoDichTien.tinh_thanh_tien(self))
            GiaoDich.giao_dich_list.append(gd)
        else:
            gd = 'Giao dịch bán ' + str(self.magiaodich) + ' - ' + str(self.ngaygiaodich) + ' - ' + self.loaitien + ' - ' + \
            str(self.soluong) + ' - ' + str(self.dongia) + \
            ' - Thành tiền: ' + str(GiaoDichTien.tinh_thanh_tien(self))
            GiaoDich.giao_dich_list.append(gd)