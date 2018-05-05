def dem_so_lan (s_find, tup):
    count = 0
    for item in tup:
        if s_find == item:
            count += 1
    return(count)

tup = ('red','green','yellow','blue','black','white','pink','orange','red','blue')

forward = int(input('Nhập index từ 0 đến %d: ' %(len(tup)-1)))
rev = int(input('Nhập index từ -1 đến %d: ' %(-len(tup))))
s_find = input('Nhập chuỗi s_find: ')

print('Tuple = ', tup)
print('tup[%d] = ' % forward,tup[forward])
print('tup[%d] = ' % rev, tup[rev])

if s_find in tup:
    #print(s_find, 'xuất hiện trong tup', tup.count(s_find), 'lần')
    print(s_find, 'xuất hiện trong tup', dem_so_lan(s_find, tup), 'lần')
else: 
    print(s_find, 'không xuất hiện trong tup')