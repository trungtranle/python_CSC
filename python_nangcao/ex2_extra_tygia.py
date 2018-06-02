from ex2_1_JSON_lib import read_json_from_url
import json
from pprint import pprint
from textwrap import indent


class NgoaiTe(object):
    def __init__(self, type_code, imageurl, muatienmat, muack, bantienmat, banck):
        self.type = type_code
        self.imageurl = imageurl
        self.muatienmat = muatienmat
        self.muack = muack
        self.bantienmat = bantienmat
        self.banck = banck


url = 'http://phuong13021982.pythonanywhere.com/static/rateDongA.json'
data = read_json_from_url(url)
# pprint(data['items'])
dict_ngoaite = {}
for item in data['items']:
    dict_ngoaite[item['type']] = NgoaiTe(
        item['type'], item['imageurl'], item['muatienmat'], item['muack'], item['bantienmat'], item['banck'])

f = open('python_nangcao/ngoaite.json', 'w')
json.dump(data, f, indent = 4)

ma_ngoaite = input('Nhập mã ngoại tệ: ')
ma_ngoaite = ma_ngoaite.upper()
loaigiaodich = int(input('Mua:1 , Bán:0 \t'))
if loaigiaodich == 1:
    giaodich = int(input('Mua tiền mặt: 1, Mua chuyển khoản: 0 \t'))
    if giaodich == 1:
        tygia = dict_ngoaite[ma_ngoaite].muatienmat
    elif giaodich == 0:
        tygia = dict_ngoaite[ma_ngoaite].muack
elif loaigiaodich == 0:
    giaodich = int(input('Bán tiền mặt: 1, Bán chuyển khoản: 0 \t'))
    if giaodich == 1:
        tygia = dict_ngoaite[ma_ngoaite].bantienmat
    elif giaodich == 0:
        tygia = dict_ngoaite[ma_ngoaite].banck

soluong = eval(input('Số lượng giao dịch: \t'))
thanh_tien = soluong * eval(tygia)
print('Thành tiền', thanh_tien)
