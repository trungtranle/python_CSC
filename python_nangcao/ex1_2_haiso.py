from ex1_2_haiso_lib import Haiso 


a = eval(input('Nhập số thứ nhất: '))
b = eval(input('Nhập số thứ hai: '))
so = Haiso(a, b)

try:
    Haiso.in_ket_qua(so)
except ZeroDivisionError:
    print('Số thứ hai = 0, không tính thương')
