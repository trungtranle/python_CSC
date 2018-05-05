def dic_input(dic):
    i = 1
    while i == 1:
        key = input('Nhập key thứ %d: ' % (len(dic)+1))
        val = input('Nhập val thứ %d: ' % (len(dic)+1))
        dic[key] = val
        i = int(input('Tiếp tục: 1, Dừng: 0 \t'))


dic = {}
dic_input(dic)
for key in sorted(dic):
    print(key, ':', dic[key])
