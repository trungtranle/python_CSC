from tinh_tien_nuoc_lib import tinh_tien_nuoc

try:
    so_khoi = eval(input('Nhập số khối: '))
    thanh_tien = tinh_tien_nuoc(so_khoi)
except AssertionError:
    print('Số khối nhập không hợp lệ!')
else:
    print('Tiền nước: ', thanh_tien, 'VND')
