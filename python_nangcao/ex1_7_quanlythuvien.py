from ex1_7_quanlythuvien_lib import Sachgiaokhoa, Sachthamkhao

i = 1
while i == 1:
    masach = input('Mã sách: \t')
    tensach = input('Tên sách: \t')
    ngaynhap = input('Ngày nhập: \t')
    dongia = eval(input('Đơn giá: \t'))
    soluong = int(input('Số lượng: \t'))
    nxb = input('Nhà xuất bản: \t')
    loai_condition = 1
    while loai_condition == 1: 
        try:
            loai = int(input('Sách giáo khoa hay sách tham khảo? SGK: 1, Sách tham khảo:0 \t'))
            assert (loai == 1 or loai == 0)
            loai_condition = 2
        except (ValueError, AssertionError):
            print('Loại sách không đúng')
    if loai == 1:
        tinhtrang_condition = 1
        while tinhtrang_condition == 1: 
            try:
                tinhtrang = int(input('Tình trạng \t Sách mới:1   Sách cũ: 0 \t'))
                assert (tinhtrang == 1 or tinhtrang == 0)
                tinhtrang_condition = 2
            except (ValueError, AssertionError):
                print('Tình trạng sách không đúng')
        sach = Sachgiaokhoa(masach, tensach, ngaynhap, dongia, soluong, nxb, tinhtrang)
        sach.in_sach()
    else: 
        thue_condition = 1
        while thue_condition == 1: 
            try:
                thue = eval(input('Nhập thuế: 0 - 20 (%) \t'))
                assert (thue >= 0 and thue <= 20)
                thue_condition = 2
            except (ValueError, AssertionError):
                print('Thuế không đúng')
        sach = Sachthamkhao(masach, tensach, ngaynhap, dongia, soluong, nxb, thue)
        sach.in_sach()
    i = int(input('Tiếp tục? Có: 1   Ngừng: 0 \t'))