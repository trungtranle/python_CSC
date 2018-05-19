class Phuong_trinh_bac_nhat(object):

    def __init__(self, a , b):
        self.a = a
        self.b = b
    
    def tinh_nghiem(self):
        if self.a == 0 and self.b != 0:
            return 'Phương trình vô nghiệm'
        elif self.a == 0 and self.b == 0:
            return 'Phương trình vô số nghiệm'
        else:
            return -self.b/self.a
    
    def in_ket_qua(self):
        print('Kết quả: ', self.tinh_nghiem())
        