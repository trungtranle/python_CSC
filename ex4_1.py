'''
Created on Apr 15, 2018

@author: hv
'''
a = eval(input('a= '))
b = eval(input('b= '))
c = eval(input('c= '))
d = eval(input('d= '))
if a >= b: 
    mx = a
else:
    mx = b

if mx <= c:
    mx = c
if mx <= d:
    mx = d
print('max=', mx)

if a <= b: 
    mn = a
else:
    mn = b

if mn >= c:
    mn = c
if mn >= d:
    mn = d
print('min=', mn)
