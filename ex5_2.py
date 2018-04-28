n = eval(input('n = '))
x = eval(input('x = '))

import math
s1 = x*x + 1
i = 1
s = math.pow (s1,n)

'''while i <= n:
    s = s * s1
    i = i + 1'''

print ('S = (x^2 + 1) ^ n = ', s)