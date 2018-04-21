n = eval(input('n = '))
x = eval(input('x = '))

s1 = x*x + 1
i = 1
s = 1
while i <= n:
    s = s * s1
    i = i + 1
print('S = (x^2 + 1) ^ n = ', s)