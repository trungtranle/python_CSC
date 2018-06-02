from ex2_1_JSON_lib import read_json_from_url
from pprint import pprint

url = "http://dev-er.com/service_api_ban_sach/api_service_sach.php"
sach = read_json_from_url(url)
#pprint(sach)
print('Số lượng sách: ', len(sach))
for item in sach:
    print(item['id'], 'Tên sách:', item['ten_sach'], 'Ngày xuất bản', item['ngay_xuat_ban'],'Giá bìa', item['gia_bia'])