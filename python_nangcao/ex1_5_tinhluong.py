from ex1_5_tinhluong_lib import Nhanvien

name = input('Nhập tên: ')
heso = eval(input('Nhập hệ số lương: '))
songuoi = eval(input('Nhập số người giảm trừ gia cảnh: '))
phucap = eval(input('Nhập phụ cấp: '))
nhanvien = Nhanvien(name, heso, songuoi, phucap)
print('--------------')
print('Họ tên: ', nhanvien.hoten)
print('Hệ số lương: ', nhanvien.heso)
print('Số người giảm trừ gia cảnh: ', nhanvien.songuoi)
print('Phụ cấp: ', format(nhanvien.phucap, ",d"))
print('Thu nhập:', format(nhanvien.thu_nhap,",f"))
print('Thuế: ', format((nhanvien.tinh_thue()),",.0f"))
print('Thực lĩnh', format((nhanvien.tinh_thuc_linh()),",.0f"))

