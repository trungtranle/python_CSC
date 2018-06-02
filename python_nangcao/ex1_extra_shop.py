from ex1_extra_shop_lib import *

cmnd = eval(input('CMND: \t'))
ten = input('Tên: \t')
email = input('Email: \t')
dienthoai = input('Điện thoại: \t')
diachi = input('Địa chỉ: \t')

khachhang = KhachHang(cmnd, ten, email, dienthoai, diachi)

ngay_dat = input('Ngày đặt: \t')
trang_thai = int(
    input('Trạng thái: 1: Vừa mới đặt, 2: Đã Thanh Toán, 3: Đã nhận hàng \t'))
xuat_hoa_don = int(input('Xuất hóa đơn: 1: Có, 0: Không \t'))
hoa_don = True
if xuat_hoa_don == 0:
    hoa_don = False

i = 1
list_item = []
while i == 1:
    tensp = input('Nhập tên sản phẩm: \t')
    soluong = eval(input('Số lượng: \t'))
    dongia = eval(input('Đơn giá: \t '))
    sanpham = Chitiet(tensp, soluong, dongia)
    list_item.append(sanpham)
    i = int(input('Tiếp tục: 1, Dừng: 0 \t'))

don_hang = Donhang(ngay_dat, trang_thai, hoa_don, list_item)

the = int(input('Thẻ tín dụng: 1, Thẻ ATM: 0 \t'))
maso = input('Số thẻ: \t')
phuongthuc = input('Phương thức: \t')
if the == 1:
    loai = input('Loại: \t')
    ngayhethan = input('Ngày hết hạn: \t')
    no_toida = eval(input('Nợ tối đa: \t'))
    the_thanhtoan = TheTinDung(maso, phuongthuc, loai, ngayhethan, no_toida)
elif the == 0:
    sotiencon = input('Số tiền còn: \t')
    the_thanhtoan = TheATM(maso, phuongthuc, sotiencon)

thanh_toan = ThanhToan(cmnd, ten, email, dienthoai, diachi,
                       ngay_dat, trang_thai, xuat_hoa_don, list_item, maso, phuongthuc)
thanh_toan.in_thanh_toan()
if the == 1:
    print('Loại:', the_thanhtoan.loai)
    print('Ngày hết hạn:', the_thanhtoan.ngayhethan)
    print('Nợ tối đa', the_thanhtoan.no_toida)
elif the == 2:
    print('Số tiền còn:', the_thanhtoan.sotiencon)
