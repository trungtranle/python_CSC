n = eval(input('n = '))
x = eval(input('x = '))

s1 = x*x + x + 1
s2 = x*x - x + 1

import math

i = 1
a = 0
a1 = 1
a2 = 1
'''
while i <= n:
    a1 = a1 * s1
    a2 = a2 * s2
    a = a1 + a2
    i = i + 1
'''
a = math.pow(s1,n) + math.pow(s2, n) 
print('A = (x^2 + x +1)^n + (x^2 - x +1)^n = ', a)
