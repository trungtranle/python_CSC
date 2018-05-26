from ex1_9_tinh_luong_lib import NhanVienKinhDoanh, NhanVienSanXuat

i = 1
nv_kinhdoanh = []
luong_kinhdoanh = []
nv_sanxuat = []
luong_sanxuat = []
while i == 1:
    j = 1
    while j == 1:
        try:
            ten = input('Tên nhân viên: \t')
            heso = eval(input('Hệ số lương: \t'))
            songuoi = int(input('Số người phụ thuộc: \t'))
            phucap = eval(input('Phụ cấp: \t'))
            loai = int(
                input('Nhân viên kinh doanh: 1, Nhân viên sản xuất: 0 \t'))
            assert(loai == 1 or loai == 0)
            j = 2
        except AssertionError:
            print('Loại nhân viên không đúng') 
            j = 1
        else:
            if loai == 1:
                try:
                    doanh_so = eval(input('Tỉ lệ lương kinh doanh: 0 - 200%: \t'))
                    assert(doanh_so >= 0 and doanh_so <= 200)
                except AssertionError:
                    print('Tỉ lệ lương kinh doanh phải từ 0 đến 200%')
                else:
                    nhan_vien = NhanVienKinhDoanh(
                        ten, heso, songuoi, phucap, doanh_so)
                    data = nhan_vien.hoten + ' - Hệ số lương: ' + str(nhan_vien.heso) + ' - Số người phụ thuộc: ' + str(nhan_vien.songuoi) + ' - Phụ cấp: ' + str(nhan_vien.phucap) + ' - Doanh số: ' + str(nhan_vien.doanhso) + ' - Thu nhập ' + str(
                        nhan_vien.tinh_thu_nhap()) + ' - Thu nhập chịu thuế ' + str(nhan_vien.tinh_thu_nhap_chiu_thue()) + ' - Thuế TNCN ' + str(nhan_vien.tinh_thue()) + ' - Thực lĩnh ' + str(nhan_vien.tinh_thuc_linh())
                    nv_kinhdoanh.append(data)
                    luong_kinhdoanh.append(nhan_vien.tinh_thu_nhap())
                    for item in nv_kinhdoanh:
                        print(item)
                    tong_luong = 0
                    for item in luong_kinhdoanh:
                        tong_luong += item
                    trung_binh = tong_luong / len(luong_kinhdoanh)
                    print('Trung bình lương NV Kinh doanh:', trung_binh)
            else:
                so_sp = int(input('Số sản phẩm: \t'))
                nhan_vien = NhanVienSanXuat(ten, heso, songuoi, phucap, so_sp)
                data = nhan_vien.hoten + ' - Hệ số lương: ' + str(nhan_vien.heso) + ' - Số người phụ thuộc: ' + str(nhan_vien.songuoi) + ' - Phụ cấp: ' + str(nhan_vien.phucap) + ' - Số sản phẩm: ' + str(nhan_vien.sosanpham) + ' - Thu nhập ' + str(
                    nhan_vien.tinh_thu_nhap()) + ' - Thu nhập chịu thuế ' + str(nhan_vien.tinh_thu_nhap_chiu_thue()) + ' - Thuế TNCN ' + str(nhan_vien.tinh_thue()) + ' - Thực lĩnh ' + str(nhan_vien.tinh_thuc_linh())
                nv_sanxuat.append(data)
                luong_sanxuat.append(nhan_vien.tinh_thu_nhap())
                for item in nv_sanxuat:
                    print(item, '\n')
                tong_luong = 0
                for item in luong_sanxuat:
                    tong_luong += item
                trung_binh = tong_luong / len(luong_sanxuat)
                print('Trung bình lương NV Sản xuất:', trung_binh)
    i = int(input('Tiếp tục: 1, Ngừng: 0 \t'))
