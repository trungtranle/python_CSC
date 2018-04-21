n = int(input('Nhập số nguyên n: '))
A = 0
A_res = 'A ='
B = 0
B_res = 'B ='
C = 1
C_res = 'C ='
D = 1
D_res = 'D = '
E = 0
E_res = 'E = '

for i in range(1,n + 1):
    if i <= n and i % 2 != 0:
        A = A + i
        A_res += str(i) + '+ ' 

for i in range(1,n + 1):
    if i <= n and i % 2 == 0:
        B = B + i
        B_res += str(i) + '+ ' 

for i in range(1,n + 1):
    C = C * i
    C_res += str(i) + '* '

for i in range(1,n + 1):
    if i <= n and i % 3 ==0:
        D = D * i
        D_res += str(i) + '* '

for i in range(1,n + 1):
    count = 0
    for x in range (1, i + 1):
        if i % x == 0:
            count += 1
    if count == 2: 
        E += i
        E_res += str(i) + '+ '
    

print(A_res,'=',A)
print(B_res,'=',B)
print(C_res,'=',C)
print(D_res,'=',D)
print(E_res,'=',E)

