tup = ('red','green','yellow','blue','black','white','pink','orange','red','blue')

forward = int(input('Nhập index từ 0 đến %d: ' %(len(tup)-1)))
rev = int(input('Nhập index từ -1 đến %d: ' %(-len(tup))))
s_find = input('Nhập chuỗi s_find: ')

print('Tuple = ', tup)
print('tup[%d] = ' % forward,tup[forward])
print('tup[%d] = ' % rev, tup[rev])

if s_find in tup:
    print(s_find, 'xuất hiện trong tup', tup.count(s_find), 'lần')
else: 
    print(s_find, 'không xuất hiện trong tup')