from ex08__lib_matrix import *

col = int(input('Nhập số cột: '))
row = int(input('Nhập số dòng: '))

matrix = matrix_create (col, row)
print('Ma trận 1')
matrix_print(matrix)
print('Các số chính phương trong ma trận 1')
matrix_square_check(matrix)
matrix_2 = matrix_replicate(matrix)
print('Ma trận 2')
matrix_print(matrix_2)
matrix_3 = matrix_add(matrix, matrix_2)
print('Ma trận 3')
matrix_print(matrix_3)