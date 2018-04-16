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

if a <= b:
    mn1 = a 
else:
    mn1 = b

if c <= d:
    mn2 = c
else:
    mn2 = d

if mn1 <= mn2:
    mn = mn1
else: 
    mn = mn2

print('Min = ', mn)         

x = eval(input('Tiếp: 0 = No, 1 = Yes: '))




