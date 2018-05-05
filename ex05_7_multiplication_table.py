tu = eval(input('Từ: '))
den = eval(input('Đến: '))
a = 1
re = ''

for j in range(1, 11):
    for i in range(tu, den+1):
        a = i * j
        re += str(i) + ' x ' + str(j) + ' = ' + str(a) + '\t'
    re += '\n'

print(re)
