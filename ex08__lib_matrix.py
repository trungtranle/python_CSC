import random
import math


def matrix_create(col, row):
    matrix = []
    for i in range(0, row):
        row_i = []
        for j in range(0, col):
            row_i.append(random.randrange(1, 10))
        matrix.append(row_i)
    return matrix


def matrix_print(matrix):
    result = ''
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            result = result + str((matrix[i][j])) + '\t'
        result = result + '\n'
    print(result)


def matrix_square_check(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if math.modf(math.sqrt(matrix[i][j]))[0] == 0:
                print('[%d] [%d] = %d' % (i, j, matrix[i][j]))


def matrix_replicate(matrix_original):
    matrix = []
    for i in range(0, len(matrix_original)):
        row_i = []
        for j in range(0, len(matrix_original[i])):
            row_i.append(random.randrange(1, 10))
        matrix.append(row_i)
    return matrix


def matrix_add(matrix_1, matrix_2):
    matrix_result = []
    for i in range(0, len(matrix_1)):
        row_i = []
        for j in range(0, len(matrix_1[i])):
            row_i.append(matrix_1[i][j] + matrix_2[i][j])
        matrix_result.append(row_i)
    return matrix_result
