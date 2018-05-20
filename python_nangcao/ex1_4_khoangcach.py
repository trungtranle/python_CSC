from ex1_4_khoangcach_lib import *

x_a = eval(input('Nhập A(x) = '))
y_a = eval(input('Nhập A(y) = '))
x_b = eval(input('Nhập B(x) = '))
y_b = eval(input('Nhập B(y) = '))

A = Diem(x_a, y_a)
B = Diem(x_b, y_b)

AB = Duongthang(A, B)
khoang_cach = Duongthang.tinh_do_dai_segment(AB)

print('Khoảng cách = ', round(khoang_cach,))

'''
area = tinh_dien_tich_hinh_tron(A, B)
circumfrence = tinh_chu_vi_hinh_tron(A, B)

area_hcn = tinh_dien_tich_hcn(A, B)
perimeter = tinh_chu_vi_hcn(A, B)

print('Diện tích hình tròn', round(area, 2))
print('Chu vi hình tròn', round(circumfrence, 2))
print('Diện tích hình chữ nhật', area_hcn)
print('Chu vi hình chữ nhật', perimeter)
'''
