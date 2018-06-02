from ex2_1_JSON_lib import read_json_from_url
from pprint import pprint

url = 'http://dev-er.com/service_api_ban_sach/api_service_sach.php?task=sach_noi_bat'
sach_noi_bat = read_json_from_url(url)
#pprint(sach_noi_bat)
print('Danh sách sách nổi bật')
for item in sach_noi_bat:
    print(item['id'], ' - Tên sách:', item['ten_sach'], '- Tên tác giả:', item['ten_tac_gia'], ' - Ngày xuất bản:', item['ngay_xuat_ban'], ' - Giá bìa:', item['gia_bia'], '- Giới thiệu:', item['gioi_thieu'][0:200])