a = eval(input('Nhập a: '))
b = eval(input('Nhập b: '))
c = eval(input('Nhập c: '))
d = eval(input('Nhập d: '))

if a >= b:
    mx1 = a 
else:
    mx1 = b

if c >= d:
    mx2 = c
else:
    mx2 = d

if mx1 >= mx2:
    mx = mx1
else: 
    mx = mx2

print('Max = ', mx)         
