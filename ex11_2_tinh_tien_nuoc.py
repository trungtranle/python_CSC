from ex11_2_lib_tinh_tien_nuoc import tinh_tien_nuoc

try:
    doituong = int(input('Nhập đối tượng: GB'))
    usage = eval(input('Nhập số nước (m3): '))
    tien_nuoc = tinh_tien_nuoc(usage=usage, doituong=doituong)
except AssertionError as er1:
    print('Lỗi: Không tồn tại đối tượng GB%d' % doituong)
    a = 0
except (NameError, SyntaxError) as er2:
    print('Lỗi: Nhập số nước dạng số')
else:
    tien_nuoc = tinh_tien_nuoc(usage=usage, doituong=doituong)
    print('Tổng tiền phải trả:', tien_nuoc, 'VNĐ')
