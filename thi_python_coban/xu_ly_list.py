from xu_ly_list_lib import *

list_1 = []
list_1 = nhap_list(list_1)
print('List: ', list_1)

in_tung_phan_tu(list_1)

phan_tu_dai_nhat(list_1)

s_find = input('Nhập giá trị cần tìm: ')
tim_phan_tu(list_1, s_find)

print_sorted(list_1)
