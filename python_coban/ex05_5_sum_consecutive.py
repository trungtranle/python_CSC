n = int(input('Nhập số nguyên n: '))
A = 0
A_res = 'A = '
B = 0
B_res = 'B = '
C = 1
C_res = 'C = '
D = 1
D_res = 'D = '
E = 0
E_res = 'E = '

for i in range(1, n + 1):
    if i <= n and i % 2 != 0:
        A = A + i
        A_res += str(i) + ' + '

for i in range(1, n + 1):
    if i <= n and i % 2 == 0:
        B = B + i
        B_res += str(i) + ' + '

for i in range(1, n + 1):
    C = C * i
    C_res += str(i) + ' * '

for i in range(1, n + 1):
    if i <= n and i % 3 == 0:
        D = D * i
        D_res += str(i) + ' * '

for i in range(1, n + 1):
    count = 0
    for x in range(1, i + 1):
        if i % x == 0:
            count += 1
    if count == 2:
        E += i
        E_res += str(i) + ' + '


print(A_res[:(len(A_res)-2)], '=', A)
print(B_res[:(len(B_res)-2)], '=', B)
print(C_res[:(len(C_res)-2)], '=', C)
print(D_res[:(len(D_res)-2)], '=', D)
print(E_res[:(len(E_res)-2)], '=', E)
