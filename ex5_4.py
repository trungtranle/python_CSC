x = eval(input('x = '))
count = 0
for i in range(1,x+1):
    if x % i == 0:
        count = count + 1
if count == 2:
    print(x,'là số nguyên tố')
else: 
    print (x, 'không phải là số nguyên tố')        

