def nhap_list(list_1):
    i = 1
    while i == 1:
        content = input('Nhập giá trị: \t')
        list_1.append(content)
        i = int(input('Tiếp tục nhập giá trị? 1: Có, 0: Không \t'))
    return list_1


def in_tung_phan_tu(list_1):
    print('Giá trị : Chiều dài phần tử')
    for item in list_1:
        ket_qua = '('
        ket_qua = ket_qua + item + ' : ' + str(len(item)) + ')'
        print(ket_qua)


def phan_tu_dai_nhat(list_1):
    print('Các phần tử dài nhát:')
    mx = len(list_1[0])
    for i in range(0, len(list_1)):
        if mx < len(list_1[i]):
            mx = len(list_1[i])
    result = []
    for i in range(0, len(list_1)):
        if len(list_1[i]) == mx:
            result.append(i)
    for item in result:
        print(item, ' : ', list_1[item], ' : ', mx)


def tim_phan_tu(list_1, search):
    if search in list_1:
        print('Các vị trí có giá trị giống', search, ":", list_1.index(search))
    else:
        print('Không có phần tử nào giống', search)


def print_sorted(list_1):
    print('List sau khi sắp xếp:')
    print(sorted(list_1))
