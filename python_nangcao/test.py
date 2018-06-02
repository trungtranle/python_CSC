'''
import json
from textwrap import indent
from pprint import pprint
from ex2_1_JSON_lib import read_json_from_file


class PhongKaraoke(object):
    def __init__(self, id_1, ten, maso, loaiphong, dongia, sokhachtoida, trangthai):
        self.id = id_1
        self.ten = ten
        self.maso = maso
        self.loaiphong = loaiphong
        self.dongia = dongia
        self.sokhachtoida = sokhachtoida
        self.trangthai = trangthai


id_1 = input('ID: \t')
ten = input('Tên: \t')
maso = input('Mã số phòng: \t')
loaiphong = int(input('Mã số loại phòng (1, 2 hoặc 3): \t'))
dongia = eval(input('Đơn giá: '))
sokhachtoida = int(input('Số khách tối đa: \t'))
trangthai = input('Trạng thái: CON_TRONG hoặc CO_KHACH: \t')

phong = PhongKaraoke(id_1, ten, maso, loaiphong,
                     dongia, sokhachtoida, trangthai)

phong_data = {'ID': phong.id, 'Tên': phong.ten, 'Mã số': phong.maso, 'Loại': phong.loaiphong,
              'Đơn giá': phong.dongia, 'Số khách': phong.sokhachtoida, 'Trạng thái': phong.trangthai}
#phong_data2 = {phong.id : phong_data}
f = open('python_nangcao/qly_phong_karaoke.json',  encoding='utf-8')
data = json.load(f)
data.update(phong_data)
f = open('python_nangcao/qly_phong_karaoke.json', 'a', encoding='utf-8')
json.dump(data, f, indent=4)
f.close()

f = open('python_nangcao/qly_phong_karaoke.json',  encoding='utf-8')
data = json.load(f)
pprint(data)
'''
import xml.dom.minidom 
f = xml.dom.minidom.parse('python_nangcao/student.xml')
root = f.documentElement
if root.hasAttribute('shelf'):
    print(root.getAttribute('shelf'))

    #contacts = root.getElementsByTagname('contact')
contacts = f.documentElement.getElementsByTagname('student')
i = 1
for contact in contacts:
    print('---Contact #%d----' % i)
    if contact.hasAttribute('id'):
        print('Name =', contact.getAttribute('id'))
        #print('Phone = ', contact.getAttribute('phone'))
    i += 1