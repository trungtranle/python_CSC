def in_dictionary (dic):
    for key, value in dic.items():
        print(key, ':', value, '\n')

def tim_kiem_dictionary (dic, key_search):
    if key_search in dic.keys():
        print(key_search, ':', directory.get(dic))
    else:
        print('Không tìm thấy', key_search)

def them_dictionary (dic, key_insert, value_insert):
    dic[key_insert] = value_insert
    return dic

def xoa_dic (dic, key_remove):
    if key_remove in dic.keys():
        i = int(input('Bạn có thực sự muốn xóa? Yes = 1, No = 0 \t'))
        if i == 1: 
            del dic[key_remove]
            print ('Đã xóa từ', key_remove)
    else: 
        print(key_remove, 'không có trong dictionary')

directory = {'Johnny' : '0787084', 'Katherine' : '14546465456', 'Misu' : 454560540, 'Jack' : 45456}

cont = 1 
while cont == 1:
    task = int(input('Bạn muốn làm gì? 1: Xem danh bạ, 2: Tìm kiếm, 3: Thêm mới \n'))
    if task == 1:
        print('Danh bạ')
        print('Tên \t Số điện thoại')
        in_dictionary(directory)
        '''
        for key, value in directory.items():
            print(key,'\t', value)
        '''
    if task == 2: 
        find = input('Nhập tên cần tìm: ')
        '''
        if find in directory.keys():
            print(find, 'có số điện thoại', directory.get(find))
        else:
            print(find, 'không có trong danh bạ')
        '''
        tim_kiem_dictionary (directory, find)

    if task == 3:
        key = input('Nhập tên: \t')
        '''
        directory[key] = input('Nhập số điện thoại: \t')
        print(key, '\t', directory.get(key))
        '''
        value = input('Nhập số điện thoại: \t')
        them_dictionary (directory, key, value)
        
    cont = int(input('Tiếp tục? Tiếp: 1; Không tiếp: 0 \t'))