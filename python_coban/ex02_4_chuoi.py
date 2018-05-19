'''
Created on Apr 15, 2018

@author: hv
'''
s1 = input('Nhập chuỗi s1: ')
s2 = input('Nhập chuỗi s2: ')
s3 = input('Nhập chuỗi s3: ')
index = int(input('Nhập index: '))

print('Chiều dài chuỗi s1', len(s1))
print('Chiều dài chuỗi s2', len(s2))
print('Chiều dài chuỗi s3', len(s3))

s4 = s1[index:]
print('Chuỗi s4: ', s4)

print('Chuỗi s2 lặp lại 2 lần', s2*2)
