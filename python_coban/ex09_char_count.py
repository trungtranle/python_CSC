def dem_so_ky_tu(string):
    cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    count_majus = 0
    for i in cap:
        count_majus += string.count(i)
    count_minus = len(string) - count_majus
    return count_majus, count_minus


def dem_so_ky_tu_2(string):
    list1 = list(string)
    list2 = list(string.upper())
    count_majus = 0
    count_minus = 0
    for i in range(0, len(string)):
        if list1[i] == list2[i] and list1[i] != ' ':
            count_majus += 1
        else:
            count_minus += 1
    return count_majus, count_minus


def dem_so_ky_tu_3(string):
    count_majus = 0
    count_minus = 0
    for char in string:
        if char.isupper():
            count_majus += 1
        else:
            count_minus += 1
    print('Số chữ hoa:', count_majus)
    print('Số chữ thường:', count_minus)


'''
s = input('Nhập chuỗi s: ')
cap, uncap = dem_so_ky_tu_2(s)
print('Số ký tự hoa:', cap)
print('Số ký tự thường including space:', uncap)
'''
dem_so_ky_tu_3('abcABC')
