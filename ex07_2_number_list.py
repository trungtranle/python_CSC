def them_vao_list(list_original):
    count = 1
    while count == 1:
        list_original.append(eval(input('Nhập giá trị: ')))
        count = eval(input('Tiếp tục nhập giá trị? Có: 1, Không: 0 \n'))
    return list_original


def tinh_tong_list(list_original):
    total = 0
    for item in list_original:
        total += item
    return total


list1 = []

list1 = them_vao_list(list1)

find = eval(input('Nhập giá trị cần tìm: '))

print('List: ', list1)
#print('Tổng list =', sum (list1))
print('Tổng list = ', tinh_tong_list(list1))

if find in list1:
    print(find, 'xuất hiện', list1.count(find), 'lần trong list')
    if find >= max(list1):
        print(find, 'lớn hơn tất cả các số trong list')
    else:
        print(find, 'không lớn hơn tất cả các số trong list')
        list2 = []
        for item in list1:
            if find < item:
                list2.append(item)
        print('Các số lớn hơn', find, 'trong list:', list2)
else:
    print(find, 'không xuất hiện trong list')
