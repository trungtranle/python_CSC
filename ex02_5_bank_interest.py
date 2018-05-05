'''
Created on Apr 15, 2018

@author: hv
'''
rate = eval(input('Lãi suất 1 năm (%): '))
amount = eval(input('Số tiền gửi: '))
month = eval(input('Số tháng gửi: '))

interest = (amount*month)*(rate/12)
total = amount + interest

print('Tiền lãi = ', interest)
print('Tiền vốn + tiền lãi = ', total)
