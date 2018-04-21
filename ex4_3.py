'''
Created on Apr 15, 2018

@author: hv
'''
mo_cua_4 = 11000
duoi_31_4 = 15300
tren_31_4 = 12100

mo_cua_7 = 12000
duoi_31_7 = 16100
tren_31_7 = 13800

cho = 7500

loai = eval(input('Loại xe (chỉ nhập 4 hoặc 7): '))

while loai != 4 and loai != 7:
    print('Loại xe không đúng')
    loai = eval(input('Loại xe (chỉ nhập 4 hoặc 7): '))

km = eval(input('Số km di chuyển: '))
time = eval(input('Thời gian chờ (làm tròn theo phút): '))

if time > 5:
    tien_cho = (time-5)*cho
    print('Tiền chờ = (%d - 5) * 750 = %d'  % (time,tien_cho))
else:
    tien_cho = 0
    print('Tiền chờ = 0')

if loai == 4:
    if km < 0.8:
        tien_di_chuyen = mo_cua_4
    elif km < 31:
        tien_di_chuyen = mo_cua_4 + (km-0.8)*duoi_31_4
    else:
        tien_di_chuyen = mo_cua_4 + 30*duoi_31_4 + (km-0.8-30)*tren_31_4        
if loai == 7:
    if km < 0.8:
        tien_di_chuyen = mo_cua_7
    elif km < 31:
        tien_di_chuyen = mo_cua_7 + (km-0.8)*duoi_31_7
    else:
        tien_di_chuyen = mo_cua_7 + 30*duoi_31_4 + (km-0.8-30)*tren_31_7
print('Tiền di chuyển %d' % tien_di_chuyen)

tien_cuoc = tien_di_chuyen + tien_cho 
print('Tiền cước = %d + %d = %d' %(tien_di_chuyen,tien_cho,tien_cuoc))       