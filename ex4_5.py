'''
Created on Apr 15, 2018

@author: hv
'''
loai1 = 1260000
loai2 = 1550000
loai3 = 1830000
loai4 = 1830000
loai5 = 2120000
loai6 = 2120000
loai7 = 2540000
loai8 = 4800000

loai = eval(input('Nhập loại phòng (từ 1 đến 8): \n'))
dem = eval(input('Nhập số đêm: \n'))

if loai == 1:
    tien = dem * loai1
elif loai == 2:
    tien = dem * loai2  
elif loai == 3:
    tien = dem * loai3
elif loai == 4:
    tien = dem * loai4
elif loai == 5:
    tien = dem * loai5
elif loai == 6:
    tien = dem * loai6
elif loai == 7:
    tien = dem * loai7        
else:
    tien = dem * loai8            

if dem >= 2 and dem <= 3:
    tien = tien * 75 / 100
elif dem >= 4:
    tien = tien * 70 / 100   

print('Thành tiền', tien)