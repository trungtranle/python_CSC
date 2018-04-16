'''
Created on Apr 15, 2018

@author: hv
'''
muc1 = 1484
muc2 = 1533
muc3 = 1786
muc4 = 2242
muc5 = 2503
muc6 = 2587

kw = eval(input('Số kw tiêu thụ: '))

if kw <= 50:
    tien_dien = kw * muc1
elif kw <= 100:
    tien_dien = 50 * muc1 + (kw-50) * muc2
elif kw <= 200:
    tien_dien = 50 * muc1 + 50 *muc2 + (kw-100)*muc3
elif kw <= 300:
    tien_dien = 50 * muc1 + 50 *muc2 + 100*muc3 + (kw-200)*muc4
elif kw <= 400:
    tien_dien = 50 * muc1 + 50 *muc2 + 100*muc3 + 100*muc4 + (kw-300)*muc5
else:
    tien_dien = 50 * muc1 + 50 *muc2 + 100*muc3 + 100*muc4 + 100*muc5 + (kw-400)*muc6
    
print('Tiền điện phải trả = ',tien_dien)          