from ex11_2_lib_tinh_tien_nuoc import tinh_tien_nuoc

a = 0
while a == 0:
    a = 1
    try:
        doituong = int(input('Nhập đối tượng: GB'))
        usage = eval(input('Nhập số nước (m3): '))
        tien_nuoc = tinh_tien_nuoc(usage=usage, doituong=doituong)
    except AssertionError:
        print('Lỗi: Không tồn tại đối tượng GB%d' % doituong)
        print('Nhập lại \n')
        a = 0
    except (NameError, SyntaxError):
        print('Lỗi: Nhập số nước dạng số')
        print('Nhập lại \n')
        a = 0
    else:
        print('Tổng tiền phải trả:', tien_nuoc, 'VNĐ')
