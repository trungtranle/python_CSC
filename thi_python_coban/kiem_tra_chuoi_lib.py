def kiem_tra_chuoi(string):
    string_list = list(string)
    vowel = ['a', 'e', 'i', 'o', 'u']
    not_appear =[]
    for i in range(0,5):
        if vowel[i] in string_list:
            not_appear.append(i+1)
        else:
            not_appear.append(i)
    result = 'Còn thiếu nguyên âm '
    for i in range(0, len(not_appear)):
        if not_appear[i] == i:
            result = result + vowel[i] + ' '
    if result == 'Còn thiếu nguyên âm ':
        result = 'Tìm thấy tất cả nguyên âm'
    return result

st = 'This is a cat'
print(kiem_tra_chuoi(st))