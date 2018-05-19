list1 = []

for count in range(1, 6):
    list1.append(eval(input('Nhập phần tử thứ %d ' % count)))
print('\n')
print(list1, '\n')

print('Các cặp số chia hết cho nhau:')
for i in range(0, len(list1)):
    for j in range(0, len(list1)):
        if i == j:
            continue
        else:
            if list1[i] % list1[j] == 0:  # or list1[j] % list1[i] == 0:
                print(list1[i], '&', list1[j])

print('Các cặp số này bằng hai lần số kia:')
for i in range(0, len(list1)):
    for j in range(0, len(list1)):
        if i == j:
            continue
        else:
            if list1[i] == 2 * list1[j]:  # or list1[j] == 2 * list1[i]:
                print(list1[i], '&', list1[j])

print('Hai số cộng lại bằng 8:')
for i in range(0, len(list1)):
    for j in range(i, len(list1)):
        if i == j:
            continue
        else:
            if list1[i] + list1[j] == 8:
                print(list1[i], '+', list1[j], '= 8')

'''
list_so = [2,7,1,4,8,6,3]

chuoi_chia_het = ""
chuoi_gap_hai_lan = ""
chuoi_tong_bang_8 = ""
for i in range(0, len(list_so)-1):
    for j in range(i+1, len(list_so)):
        if list_so[i]%list_so[j]==0 or list_so[j]%list_so[i] == 0: 
            chuoi_chia_het += str(list_so[i]) + "&" + str(list_so[j]) + " ; " 
        if list_so[i]/list_so[j]==2 or list_so[j]/list_so[i] == 2: 
            chuoi_gap_hai_lan += str(list_so[i]) + "&" + str(list_so[j]) + " ; "
        if list_so[i]+list_so[j]==8 or list_so[j]+list_so[i] == 8: 
            chuoi_tong_bang_8 += str(list_so[i]) + "&" + str(list_so[j]) + " ; "     

print(chuoi_chia_het)
print(chuoi_gap_hai_lan)
    print(chuoi_tong_bang_8)
'''
