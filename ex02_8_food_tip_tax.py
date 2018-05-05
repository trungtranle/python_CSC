'''
Created on Apr 15, 2018

@author: hv
'''
total = eval(input('Tổng số tiền món ăn và thức uống: '))
tax_rate = eval(input('Thuế (10-20%): '))
tip_rate = eval(input('Tip (5-10%): '))

tax = total * tax_rate/100
tip = total * tip_rate/100
pay = total + tax + tip

print('Thuế phải trả', tax)
print('Tip', tip)
print('Tổng số tiền thanh toán', pay)
