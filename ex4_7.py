mst = input('Mã số thuế: ')
ten = input('Họ tên người nộp thuế: ')
income = eval(input('Tổng thu nhập trong một năm: '))
dep = eval(input('Số người phụ thuộc: '))

giamtru_rate = 108000000
phuthuoc_rate = 3600000 * 12

giamtru = 0

giamtru = giamtru_rate + phuthuoc_rate * dep

chiuthue = income - giamtru

muc1 = 5/100
muc2 = 10/100
muc3 = 15/100
muc4 = 20/100
muc5 = 25/100
muc6 = 30/100
muc7 = 35/100

thres1 = 60000000
thres2 = 120000000
thres3 = 216000000
thres4 = 384000000
thres5 = 624000000
thres6 = 960000000

if chiuthue <= thres1:
    thue = chiuthue * muc1
elif chiuthue <= thres2 :
    thue = thres1 * muc1 + (chiuthue - thres1) * muc2
elif chiuthue <= thres3:
    thue = thres1 * muc1 + (thres2-thres1) * muc2 + (chiuthue - thres2) * muc3
elif chiuthue <= thres4:
    thue = thres1 * muc1 + (thres2-thres1) * muc2 + (thres3-thres2) * muc3 + (chiuthue - thres3) * muc4
elif chiuthue <= thres5:
    thue = thres1 * muc1 + (thres2-thres1) * muc2 + (thres3-thres2) * muc3 + (thres4 - thres3) * muc4 + (chiuthue - thres4) * muc5
elif chiuthue <= thres6:
    thue = thres1 * muc1 + (thres2-thres1) * muc2 + (thres3-thres2) * muc3 + (thres4 - thres3) * muc4 + (thres5 - thres4) * muc5 + (chiuthue - thres5) * muc6
else: 
    thue = thres1 * muc1 + (thres2-thres1) * muc2 + (thres3-thres2) * muc3 + (thres4 - thres3) * muc4 + (thres5 - thres4) * muc5 + (thres6 - thres5) * muc6 + (chiuthue - thres6) * muc7
print('Số tiền giảm trừ',giamtru,'VND')
print('Số tiền chịu thuế',chiuthue,'VND')
print('Số thuế phải đóng',thue,'VND')