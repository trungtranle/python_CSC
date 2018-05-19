class Haiso(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def tinh_tong(self):
        tong = self.a + self.b
        return tong

    def tinh_hieu(self):
        hieu = self.a - self.b
        return hieu

    def tinh_tich(self):
        tich = self.a * self.b
        return tich

    def tinh_thuong(self):
        thuong = self.a / self.b
        return thuong

    def in_ket_qua(self):
        print('Tổng:', self.tinh_tong())
        print('Hiệu:', self.tinh_hieu())
        print('Tích:', self.tinh_tich())
        print('Thương:', self.tinh_thuong())
