from ex1_4_khoangcach_lib import Diem, tinh_khoang_cach, tinh_chu_vi_hcn, tinh_chu_vi_hinh_tron, tinh_dien_tich_hcn, tinh_dien_tich_hinh_tron, TamGiac

x_a = eval(input('Nhập A(x) = '))
y_a = eval(input('Nhập A(y) = '))
x_b = eval(input('Nhập B(x) = '))
y_b = eval(input('Nhập B(y) = '))
x_c = eval(input('Nhập C(x) = '))
y_c = eval(input('Nhập C(y) = '))

A = Diem(x_a, y_a)
B = Diem(x_b, y_b)
C = Diem(x_c, y_c)


khoang_cach = tinh_khoang_cach(A, B)

print('Khoảng cách = ', round(khoang_cach, 2))

area = tinh_dien_tich_hinh_tron(A, B)
circumfrence = tinh_chu_vi_hinh_tron(A, B)

area_hcn = tinh_dien_tich_hcn(A, B)
perimeter = tinh_chu_vi_hcn(A, B)

print('Diện tích hình tròn', round(area, 2))
print('Chu vi hình tròn', round(circumfrence, 2))
print('Diện tích hình chữ nhật', area_hcn)
print('Chu vi hình chữ nhật', perimeter)

tamgiac = TamGiac(A, B, C)
print('Diện tích tam giác ABC', round(tamgiac.tinh_dien_tich_tamgiac(),2))
