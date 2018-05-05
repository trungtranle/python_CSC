import math

def tinh_S (n, x):
    s = math.pow((x**2 + 1), n)
    return s

n = eval(input('n = '))
x = eval(input('x = '))
'''
s1 = x*x + 1
i = 1
s = math.pow (s1,n)
while i <= n:
    s = s * s1
    i = i + 1

'''

s = tinh_S (n, x)
print ('S = (x^2 + 1) ^ n = ', s)