import xml.dom.minidom as minidom


class DonVi(object):
    def __init__(self, id, ten):
        self.id = id
        self.ten = ten


class NhanVien(object):
    def __init__(self, ID, Ho_ten, Gioi_tinh, Ngay_sinh, CMND, Muc_luong, Dia_chi, ID_DON_VI):
        self.ID = ID
        self.Ho_ten = Ho_ten
        self.Gioi_tinh = Gioi_tinh
        self.Ngay_sinh = Ngay_sinh
        self.CMND = CMND
        self.Muc_luong = Muc_luong
        self.Dia_chi = Dia_chi
        self.ID_DON_VI = ID_DON_VI


def xml_donvi(list_donvi):
    f = minidom.parse('python_nangcao/don_vi.xml')
    root = f.documentElement
    donvi_s = root.getElementsByTagName('DON_VI')
    for donvi in donvi_s:
        ID = donvi.getAttribute('ID')
        ten = donvi.getAttribute('Ten')
        list_donvi.append(DonVi(ID, ten))
    return list_donvi


def xml_nhanvien(list_nhanvien):
    f = minidom.parse('python_nangcao/nhan_vien.xml')
    root = f.documentElement
    nhan_vien_s = root.getElementsByTagName('NHAN_VIEN')
    for nhanvien in nhan_vien_s:
        ID = nhanvien.getAttribute('ID')
        print(ID)
        Ho_ten = nhanvien.getAttribute('Ho_ten')
        Gioi_tinh = nhanvien.getAttribute('Gioi_tinh')
        Ngay_sinh = nhanvien.getAttribute('Ngay_sinh')
        CMND = nhanvien.getAttribute('CMND')
        Muc_luong = nhanvien.getAttribute('Muc_luong')
        Dia_chi = nhanvien.getAttribute('Dia_chi')
        ID_DON_VI = nhanvien.getAttribute('ID_DON_VI')
        list_nhanvien.append(NhanVien(
            ID, Ho_ten, Gioi_tinh, Ngay_sinh, CMND, Muc_luong, Dia_chi, ID_DON_VI))
    return list_nhanvien


def thong_ke(id, list_nhanvien):
    count = 0
    count_male = 0
    count_female = 0
    for nhanvien in list_nhanvien:
        if int(nhanvien.ID_DON_VI) == id:
            count += 1
            print(nhanvien.ID, '-', nhanvien.Ho_ten)
            if nhanvien.Gioi_tinh == 'true':
                count_male += 1
            else:
                count_female += 1
    print('Tổng số nhân viên:', count)
    print(count_male, 'Nam', count_female, 'Nữ')

def tim_kiem(name, list_nhanvien):
    for nhanvien in list_nhanvien:
        ten = nhanvien.Ho_ten.lower()
        if ten.find(name.lower()) > -1:
            print(nhanvien.ID, '-', nhanvien.Ho_ten)

list_donvi = []
list_donvi = xml_donvi(list_donvi)
list_nhanvien = []
list_nhanvien = xml_nhanvien(list_nhanvien)

print('---Danh sách đơn vị---')
i = 1
for donvi in list_donvi:
    print(donvi.id, '-', donvi.ten)

j = int(input('Chọn đơn vị (1 - 5): \t'))
thong_ke(j, list_nhanvien)

name = input('Nhập tên cần tìm: \t')
print('---Kết quả tìm kiếm---')
tim_kiem(name, list_nhanvien)

