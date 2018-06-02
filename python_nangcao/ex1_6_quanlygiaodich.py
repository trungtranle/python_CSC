from ex1_6_quanlygiaodich_lib import GiaoDichVang, GiaoDichTien
import datetime
from textwrap import indent
import json

print('Quản lý giao dịch')
giao_dich_vang = []
giao_dich_tien = []
i = 1
while i == 1:
    magiaodich = input('Nhập mã giao dịch: ')
    ngaygiaodich = input('Nhập ngày giao dịch DD/MM/YYYY: ')
    soluong = eval(input('Nhập số lượng: '))
    loaigiaodich = int(input('Nhập loại gia dịch: 1: Vàng, 2: Tiền tệ \t'))
    if loaigiaodich == 1:
        loaitien = input('Chọn loại vàng: 18k / 24k / 9999: ')
        dongia = eval(input('Nhập đơn giá: '))
        try:
            giaodich = GiaoDichVang(
                magiaodich, ngaygiaodich, dongia, soluong, loaigiaodich,  loaitien)
        except AssertionError:
            print('Loại giao dịch không đúng')
        else:
            giao_dich_vang.append({'Mã giao dịch': giaodich.magiaodich,
                                   'Ngày giao dịch': giaodich.ngaygiaodich,
                                   'Loại tiền': giaodich.loaitien,
                                   'Số lượng': giaodich.soluong,
                                   'Đơn giá': giaodich.dongia})
    else:
        loaitien = input('Chọn loại tiền: USD / EUR / AUD: ')
        dongia = eval(input('Nhập tỷ giá: '))
        muaban = int(input('Bạn muốn mua hay bán? 1: Mua, 0: Bán \t'))
        try:
            giaodich = GiaoDichTien(
                magiaodich, ngaygiaodich, dongia, soluong, loaigiaodich,  loaitien, muaban)
        except AssertionError:
            print('Loại giao dịch hoặc mua bán không đúng')
        else:
            giao_dich_tien.append({'Mã giao dịch': giaodich.magiaodich,
                                   'Ngày giao dịch': giaodich.ngaygiaodich,
                                   'Loại tiền': giaodich.loaitien,
                                   'Số lượng': giaodich.soluong,
                                   'Đơn giá': giaodich.dongia,
                                   'Loại giao dịch': muaban})

    giaodich.them_vao_danh_sach()
    giaodich.in_giao_dich_cuoi()

    i = int(input('Tiếp tục: 1, Dừng: 0 \t'))

j = int(input('Ghi vào file? Có: 1, Không: 0 \t'))
if j == 1:
    date = datetime.datetime.now()
    file_name = 'python_nangcao/' + date.strftime('%Y-%m-%d-%H-%M-%S') + '.json'
    f = open(file_name, 'w', encoding = 'utf-8')
    giaodich = {'Giao dịch tiền':giao_dich_tien, 'Giao dịch vàng':giao_dich_vang}
    json.dump(giaodich, f, indent=4) 
    f.close()
    print('Đã ghi')
