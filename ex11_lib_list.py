def list_sequence_append(list_1):
    i = 1
    while i == 1: 
        item = input('Nhập phẩn tử thứ %d: ' %(len(list_1) + 1))
        list_1.append(item)
        i = int(input('Tiếp tục? Tiếp: 1, Không: 0 \t'))
    return list_1


list_a = []
list_a = list_sequence_append(list_a)