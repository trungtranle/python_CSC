from ex1_6_quanlygiaodich_lib import GiaoDichVang, GiaoDichTien

print('Quản lý giao dịch')
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
            giaodich = GiaoDichVang(magiaodich, ngaygiaodich, dongia, soluong, loaigiaodich,  loaitien)
        except AssertionError:
            print('Loại giao dịch không đúng')   
    else:
        loaitien = input('Chọn loại tiền: USD / EUR / AUD: ')
        dongia = eval(input('Nhập tỷ giá: '))
        muaban = int(input('Bạn muốn mua hay bán? 1: Mua, 0: Bán \t'))
        try:
            giaodich = GiaoDichTien(magiaodich, ngaygiaodich, dongia, soluong, loaigiaodich,  loaitien, muaban)
        except AssertionError:
            print('Loại giao dịch hoặc mua bán không đúng')
    giaodich.them_vao_danh_sach()
    giaodich.in_giao_dich_cuoi()
    
    i = int(input('Tiếp tục: 1, Dừng: 0 \t'))