from tinh_s_h_tamgiac_lib import Tamgiac, la_tam_giac

a = eval(input('Nhập cạnh a: \t'))
b = eval(input('Nhập cạnh b: \t'))
c = eval(input('Nhập cạnh c: \t'))

if la_tam_giac(a, b, c):
    tamgiac = Tamgiac(a, b, c)
    print(Tamgiac.in_ket_qua(tamgiac))