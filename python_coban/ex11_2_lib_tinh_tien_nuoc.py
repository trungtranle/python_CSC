don_gia_sinh_hoat = {'muc_1': 6095,
                     'muc_2': 11730,
                     'muc_3': 13110}

don_gia_khong_sinh_hoat = {'san_xuat': 11040,
                           'co_quan': 11845,
                           'kinh_doanh': 19435}


def tinh_tien_nuoc_sinh_hoat(usage):
    so_nguoi = int(input('Số người trong nhà: '))
    threshold_1 = 4 * so_nguoi
    threshold_2 = 6 * so_nguoi
    if usage <= threshold_1:
        thanh_tien = don_gia_sinh_hoat['muc_1'] * usage
        print('Mức 1: đến', threshold_1, 'm3 \t Sử dụng:', usage, 'm3')
    elif usage <= threshold_2:
        thanh_tien = don_gia_sinh_hoat['muc_1'] * threshold_1 + \
            don_gia_sinh_hoat['muc_2'] * (usage - threshold_1)
        print('Mức 1: đến', threshold_1, 'm3 \6 Sử dụng:', threshold_1, 'm3')
        print('Mức 2: trên', threshold_1, 'đến', threshold_2,
              'm3 \t Sử dụng:', (usage - threshold_1), 'm3')
    else:
        thanh_tien = don_gia_sinh_hoat['muc_1'] * threshold_1 + don_gia_sinh_hoat['muc_2'] * (
            threshold_2 - threshold_1) + don_gia_sinh_hoat['muc_3'] * (usage - threshold_2)
        print('Mức 1: đến', threshold_1, 'm3\t Sử dụng:', threshold_1, 'm3')
        print('Mức 2: trên', threshold_1, 'm3 đến', threshold_2,
              'm3 \t Sử dụng:', (threshold_2 - threshold_1), 'm3')
        print('Mức 3: trên', threshold_2, 'm3',
              '\t Sử dụng:', (usage - threshold_2), 'm3')
    return thanh_tien


def tinh_tien_nuoc_khong_sinh_hoat(usage, doituong):
    if doituong == 12 or doituong == 22 or doituong == 32:
        don_gia = don_gia_khong_sinh_hoat['san_xuat']
        thanh_tien = don_gia * usage
    elif doituong == 31:
        don_gia = don_gia_khong_sinh_hoat['co_quan']
        thanh_tien = don_gia * usage
    elif doituong == 23 or doituong == 33:
        don_gia = don_gia_khong_sinh_hoat['kinh_doanh']
        thanh_tien = don_gia * usage
    return thanh_tien


def tinh_tien_nuoc(usage, doituong):
    list_doituong = [11, 21, 12, 22, 32, 31, 13, 23, 33]
    assert (doituong in list_doituong)
    if doituong == 11 or doituong == 21:
        thanh_tien = tinh_tien_nuoc_sinh_hoat(usage)
    else:
        thanh_tien = tinh_tien_nuoc_khong_sinh_hoat(usage, doituong)
    return thanh_tien
