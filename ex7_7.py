directory = {'Johnny' : '0787084', 'Katherine' : '14546465456', 'Misu' : 454560540, 'Jack' : 45456}

cont = 1 
while cont == 1:
    task = int(input('Bạn muốn làm gì? 1: Xem danh bạ, 2: Tìm kiếm, 3: Thêm mới \n'))
    if task == 1:
        print('Danh bạ')
        print('Tên \t Số điện thoại')
        for key, value in directory.items():
            print(key,'\t', value)
    if task == 2: 
        find = input('Nhập tên cần tìm: ')
        if find in directory.keys():
            print(find, 'có số điện thoại', directory.get(find))
        else:
            print(find, 'không có trong danh bạ')
    if task == 3:
        key = input('Nhập tên: \t')
        directory[key] = input('Nhập số điện thoại: \t')
        print(key, '\t', directory.get(key))
    cont = int(input('Tiếp tục? Tiếp: 1; Không tiếp: 0 \t'))