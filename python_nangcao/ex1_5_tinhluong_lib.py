class Nhanvien(object):
    canban = 1260000

    def __init__(self, hoten, heso, songuoi, phucap):
        self.hoten = hoten
        self.heso = heso
        self.songuoi = songuoi
        self.phucap = phucap
        

    def tinh_thu_nhap(self):
        thu_nhap = self.heso * Nhanvien.canban + self.phucap
        return thu_nhap

    def tinh_thu_nhap_chiu_thue(self):
        chiuthue = Nhanvien.tinh_thu_nhap(self) - 9000000 - self.songuoi * 3600000
        if chiuthue > 0:
            return chiuthue
        else: 
            return 0

    def tinh_thue(self):
        chiuthue = Nhanvien.tinh_thu_nhap_chiu_thue(self)
        muc1 = 5/100
        muc2 = 10/100
        muc3 = 15/100
        muc4 = 20/100
        muc5 = 25/100
        muc6 = 30/100
        muc7 = 35/100

        max_muc1 = 250000
        max_muc2 = 500000
        max_muc3 = 1200000
        max_muc4 = 2800000
        max_muc5 = 5000000
        max_muc6 = 8400000

        thres1 = 5000000
        thres2 = 10000000
        thres3 = 18000000
        thres4 = 32000000
        thres5 = 52000000
        thres6 = 80000000

        if chiuthue <= thres1:
            thue = chiuthue * muc1
            if thue > max_muc1:
                thue = max_muc1
        elif chiuthue <= thres2:
            thue = thres1 * muc1 + (chiuthue - thres1) * muc2
            if thue > max_muc2:
                thue = max_muc2
        elif chiuthue <= thres3:
            thue = thres1 * muc1 + (thres2-thres1) * \
                muc2 + (chiuthue - thres2) * muc3
            if thue > max_muc3:
                thue = max_muc3
        elif chiuthue <= thres4:
            thue = thres1 * muc1 + (thres2-thres1) * muc2 + \
                (thres3-thres2) * muc3 + (chiuthue - thres3) * muc4
            if thue > max_muc4:
                thue = max_muc4
        elif chiuthue <= thres5:
            thue = thres1 * muc1 + (thres2-thres1) * muc2 + (thres3-thres2) * \
                muc3 + (thres4 - thres3) * muc4 + (chiuthue - thres4) * muc5
            if thue > max_muc5:
                thue = max_muc5
        elif chiuthue <= thres6:
            thue = thres1 * muc1 + (thres2-thres1) * muc2 + (thres3-thres2) * muc3 + (
                thres4 - thres3) * muc4 + (thres5 - thres4) * muc5 + (chiuthue - thres5) * muc6
            if thue > max_muc6:
                thue = max_muc6
        else:
            thue = thres1 * muc1 + (thres2-thres1) * muc2 + (thres3-thres2) * muc3 + (thres4 - thres3) * \
                muc4 + (thres5 - thres4) * muc5 + (thres6 - thres5) * \
                muc6 + (chiuthue - thres6) * muc7
        return thue

    def tinh_thuc_linh(self):
        thuc_linh = Nhanvien.tinh_thu_nhap(self) - Nhanvien.tinh_thue(self)
        return thuc_linh
