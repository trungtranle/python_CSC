def tao_danh_sach_su_kien (dic):
    i = 1
    while i == 1:
        ngay_gio = input('Nhập ngày giờ theo yyyy_mm_dd_hh_mm \t')
        ngay_gio_list = ngay_gio.split('_')
        list_2 = []
        for item in ngay_gio_list:
            list_2.append(int(item))   
        dieu_kien = True 
        if len(list_2) > 5: #kiem tra khong nhap du
            dieu_kien = False        
        if list_2[1] > 12 or list_2[1] < 1: #kiem tra dieu kien thang
            dieu_kien = False
        if list_2[2] > 31 or list_2[2] < 1:#kiem tra dieu kien ngay
            dieu_kien = False
        if list_2[3] > 24: # kiem tra dieu kien gio
            dieu_kien = False
        if list_2[4] > 59: # kiem tra dieu kien phut
            dieu_kien = False
        if list_2[1] in [1, 3, 5, 7, 8, 10, 12] and list_2[2] > 31: #kiem tra thang 31 ngay
            dieu_kien = False
        if list_2[1] in [4, 6, 9, 11] and list_2[2] > 30: #kiem tra thang 30 ngay
            dieu_kien = False
        if list_2[1] == 2 and list_2[2] > 29: #kiem tra thang 2, chua kiem tra nam nhuan, co thoi gian lam sau
            dieu_kien = False
        assert (dieu_kien)
        su_kien = input('Nhập sự kiện\t')
        dic[ngay_gio] = su_kien
        i = int(input('Tiếp tục nhập? Có: 1, Không: 0 \t'))
    return dic
    

def in_su_kien(dic):
    print('Các sự kiện')
    print('Thời gian : \t Sự kiện')
    for key, value in dic.items():
        print(key, ':', value)


def tim_su_kien(dic, content):
    not_found = True
    for item in dic.keys():
        dic_val_str = str(dic.get(item))
        f = dic_val_str.find(content)
        if dic_val_str.find(content) > -1:
            not_found = False
            print('Ngày giờ:', item, 'Sự kiện:', dic_val_str)
    if not_found:
        print('Không tìm thấy sự kiện nào') 
        
def thong_ke_thang_5 (dic):
    dic_key = dic.keys()
    count = 0
    for item in dic_key:
        dic_key_str = str(item)
        dic_key_split = dic_key_str.split('_')
        if dic_key_split[0] == '2018' and dic_key_split[1] == '05':
            count += 1
    print('Có %d sự kiện diễn ra trong tháng 05/2018' %count)

