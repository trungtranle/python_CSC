from ex1_4_khoangcach_lib import tinh_khoang_cach, Diem

x_a = eval(input('Ax = '))
y_a = eval(input('Ay = '))
x_b = eval(input('Bx = '))
y_b = eval(input('By = '))
x_c = eval(input('Cx = '))
y_c = eval(input('Cy = '))

A = Diem(x_a, y_a)
B = Diem(x_b, y_b)
C = Diem(x_c, y_c)

AB = tinh_khoang_cach(A,B)
BC = tinh_khoang_cach(B, C)
CA = tinh_khoang_cach(C, A)

print('AB = ', AB)
print('BC = ', BC)
print('CA = ', CA)

