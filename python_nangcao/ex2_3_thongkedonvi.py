from ex2_1_JSON_lib import read_json_from_file
from pprint import pprint

data = read_json_from_file('python_nangcao/QLCT_1.json')
#pprint(data)
print('Tên công ty:', data['CONG_TY'][0]['Ten'])
print('Địa chỉ:', data['CONG_TY'][0]['Dia_chi'])
tong_nhanvien = 0 
for donvi in data['DON_VI']:
    tong_nhanvien += eval(donvi['So_Nhan_vien'])
print('Tổng số nhân viên:', tong_nhanvien)
print('----Thống kê nhân viên theo đơn vị---')
for donvi in data['DON_VI']:
    print(donvi['ID'],'/ Tên đơn vị:', donvi['Ten'])
    print('\t - Số nhân viên:', donvi['So_Nhan_vien'])
    print('\t - Tỷ lệ:', donvi['Ty_le'])