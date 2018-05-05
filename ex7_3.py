import random
from functools import reduce 
'''
def prime_check (x):
    count = 0
    for i in range(1,x+1):
        if x % i == 0:
            count = count + 1
    return count == 2
'''
from ex5_4_so_nguyen_to import prime_check

def average_and_print_if_not_null (list_original, criteria):
    if len(list_original) > 0:
        print('Các số', criteria, ':', list_original)
        print('Trung bình cộng các phần tử', criteria, ':', (sum(list_original)/len(list_original)) )
    else:
        print('Không có phần tử', criteria)

list1 = []
count = eval(input('Số phần tử trong list: '))
'''
for i in range (1,count+1):
    list1.append(int(input('Nhập phần tử thứ %d: ' % i)))
'''

for i in range (1, count + 1):
    list1.append(random.randrange(-10,30))
print (list1)

'''
for i in range (1, count + 1):
    x = random.randrange(10,30)
    while x % 5 != 0:
        x = random.randrange(10,30)
    else:
        list1.append(x)
'''        
print (list1)
'''
list2 = []
for item in list1:
    count1 = 0
    for j in range (1, item + 1):
        if item % j == 0:
            count1 += 1
    if count1 == 2:
        list2.append(item)
print('Các số nguyên tố:', list2)
print ('Tổng các số nguyên tố = ', sum(list2))
'''
list2 = list(filter(lambda item: prime_check(item), list1))
print('Các số nguyên tố: ', list2)
list2_sum = reduce(lambda item1, item2: item1+item2, list1)
print('Tổng các số nguyên tố = ', list2_sum)

'''
list3 = []
for item in list1:
    if item > 0:
        list3.append(item)
        '''
list3 = list(filter(lambda item: item > 0,list1))
criterion_1 = 'Dương'
average_and_print_if_not_null(list3, criterion_1)

list4 = list(filter(lambda item: item < 0, list1))
criterion_2 = 'Âm'
average_and_print_if_not_null(list4, criterion_2) 

'''
if len(list3) > 0:
    print('Các số dương:', list3)
    print('Trung bình cộng các phần tử dương:', (sum(list3)/len(list3)))
else:
    print('Không có phần tử dương')
'''
'''
list4 = []
for item in list1:
    if item < 0:
        list4.append(item)
        

if len(list4) > 0:
    print('Các số âm:', list4)
    print('Trung bình cộng các phần tử âm:', (sum(list4)/len(list4)))
else:
    print('Không có phần tử âm')
'''
list4 = list(filter(lambda item: item < 0, list1))

print('Giá trị lớn nhất trong list:', max(list1))
print('Giá trị nhỏ nhất trong list:', min(list1))
list1.sort()
print('Sắp xếp theo giá trị tăng dần', list1)
list1.sort(reverse=True)
print('Sắp xếp theo giá trị giảm dần', list1)