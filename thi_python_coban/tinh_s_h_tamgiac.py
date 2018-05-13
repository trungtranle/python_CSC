from tinh_s_h_tamgiac_lib import *

a = eval(input('Nhập cạnh a: \t'))
b = eval(input('Nhập cạnh b: \t'))
c = eval(input('Nhập cạnh c: \t'))

triangle = la_tam_giac(a, b, c)
if triangle:
    area = tinh_dien_tich(a, b, c)
    print('Diện tích tam giác = ', area)
    ha = tinh_chieu_cao(area, a)
    print('ha = ', ha)
    hb = tinh_chieu_cao(area, b)
    print('hb = ', hb)
    hc = tinh_chieu_cao(area, c)
    print('hc = ', hc)
