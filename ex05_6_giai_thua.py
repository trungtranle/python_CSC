n = eval(input('Nhập n: '))
giaithua = 1
giaithua_res = ''
giaithua2 = 1
giaithua2_res = ''
for i in range(1, n+1):
    giaithua *= i
    giaithua_res += str(i) + ' x '
if n % 2 == 0:
    for i in range(1, n+1):
        if i % 2 == 0:
            giaithua2 *= i
            giaithua2_res += str(i) + ' x '

if n % 2 != 0:
    for i in range(1, n+1):
        if i % 2 != 0:
            giaithua2 *= i
            giaithua2_res += str(i) + ' x '

print(giaithua_res[:(len(giaithua_res)-3)], '=', giaithua)
print(giaithua2_res[:(len(giaithua2_res)-3)], '=', giaithua2)
