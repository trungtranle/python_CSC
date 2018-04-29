dic = {'cat' : 'mòe', 'dog' : 'Đức', 'ant' : 'kiến', 'bear' : 'gấu', 'spider' : 'nhện'}

cont = 1 
while cont == 1:
    task = int(input('Bạn muốn làm gì? 1: Xem từ điển, 2: Tìm kiếm, 3: Thêm từ mới  4: Xóa từ \n'))
    if task == 1:
        print('Từ điển')
        print('Từ \t Nghĩa')
        for key, value in dic.items():
            print(key,'\t', value)
    if task == 2: 
        find = input('Nhập từ cần tìm: ')
        if find in dic.keys():
            print(find, 'nghĩa là', dic.get(find))
        else:
            print(find, 'không có trong từ điển')
    if task == 3:
        key = input('Nhập từ: \t')
        dic[key] = input('Nhập nghĩa của từ %s: \t' % key)
        print(key, '\t', dic.get(key))
    if task == 4:
        de = input('Nhập từ cần xóa: \t')
        if de in dic.keys():
            i = int(input('Bạn có thực sự muốn xóa? Yes = 1, No = 0 \t'))
            if i == 1: 
                del dic[de]
                print ('Đã xóa từ', de)
        else: 
            print(de, 'không có trong từ điển')
    cont = int(input('Tiếp tục? Tiếp: 1; Không tiếp: 0 \t'))