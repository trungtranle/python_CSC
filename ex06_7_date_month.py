from datetime import datetime
import calendar

day = int(input('Nhập ngày: '))
month = int(input('Nhập tháng: '))
year = int(input('Nhập năm: '))

date1 = datetime(year, month, day)
print('Ngày tháng năm: ', date1.strftime('%d - %m - %Y'))
date2 = calendar.weekday(year, month, day)
'''
if date2 == 0:
    date3 = 'Thứ hai'
elif date2 == 1:
    date3 = 'Thứ ba'
elif date2 == 2:
    date3 = 'Thứ tư'
elif date2 == 3:
    date3 = 'Thứ năm'
elif date2 == 4:
    date3 = 'Thứ sáu'
elif date2 == 5:
    date3 = 'Thứ bảy'
else:
    date3 = 'Chủ nhật'
'''
weekd = ('Thứ hai', 'Thứ ba', 'Thứ tư', 'Thứ năm',
         'Thứ sáu', 'Thứ bảy', 'Chủ nhật')
print(date1.strftime('%d - %m - %Y'), 'là', weekd[date2])

if calendar.isleap(year) == True:
    print(year, 'là năm nhuận')
else:
    print(year, 'không là năm nhuận')

print('Tháng', month, 'có', calendar.monthrange(year, month)[1], 'ngày')
