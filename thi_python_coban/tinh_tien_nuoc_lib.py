def tinh_tien_nuoc(so_khoi):
    don_gia = 10000
    don_gia_2 = don_gia + don_gia * 15/100
    don_gia_3 = don_gia + don_gia * 20/100
    assert (so_khoi >= 0)
    if so_khoi <= 4:
        thanh_tien = don_gia * so_khoi
    elif so_khoi < 10:

        thanh_tien = 4 * don_gia + (so_khoi - 4) * don_gia_2
    else:
        thanh_tien = 4 * don_gia + 6 * don_gia_2 + (so_khoi - 10) * don_gia_3
    return thanh_tien
