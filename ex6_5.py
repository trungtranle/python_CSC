a = eval (input('a = '))
b = eval (input('b = '))
c = eval (input('c = '))

delta = 0

import math

if a == 0: 
    if b == 0 and c != 0:
        print ('Phương trình vô nghiệm') 
    elif b == 0 and c == 0:
        print ('Phương trình vô số nghiệm')
    else: 
        print ('Phương trình có nghiệm  x = ', -c/b)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print ('Phương trình vô nghiệm')
    elif delta == 0:
        print ('Phương trình có nghiệm kép: x1 = x2 = ', -b/2*a)
    else:
        print ('Phương trình có hai nghiệm x1 = ',(-b + math.sqrt(delta)/(2*a)),'x2 = ',(-b - math.sqrt(delta)/(2*a)))