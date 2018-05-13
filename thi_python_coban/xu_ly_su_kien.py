from xu_ly_su_kien_lib import * 

dic = {}
i = 1
while i == 1:
    try:
        dic = tao_danh_sach_su_kien(dic)
        i = 0
    except (AssertionError, TypeError, ValueError, IndexError):
        print('Nhập định dạng ngày giờ không đúng, vui lòng nhập lại')
        i = 1
    else: 
        in_su_kien(dic)
        s_find = input('Nhập sự kiện cần tìm \t')
        tim_su_kien(dic, s_find)
        thong_ke_thang_5(dic)

