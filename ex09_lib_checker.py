def checkerboard_create(size):
    checker = ''
    for i in range(1, size):
        if i % 2:
            for j in range(1, size):
                if j % 2 == 0:
                    checker = checker + '|#|'
                else:
                    checker = checker + '| |'
        else:
            for j in range(1, size):
                if j % 2 == 0:
                    checker = checker + '| |'
                else:
                    checker = checker + '|#|'

        checker = checker + '\n'
    return checker

def checker_matrix_create(size):
    checker = []
    for i in range (0, size):
        checker_i = []
        if i % 2:
            for j in range(0, size):
                if j % 2 == 0:
                    checker_i.append('|#|')
                else:
                    checker_i.append('| |')
        else:
            for j in range(0, size):
                if j % 2 == 0:
                    checker_i.append('| |')
                else:
                    checker_i.append('|#|')
        checker.append(checker_i)
    return checker
        
def checker_matrix_print(matrix):
    checker = ''
    for i in range (0, len(matrix)):
        for j in range (0, len(matrix)):
            checker += matrix[i][j]
        checker += '\n'
    print (checker)

checker = checker_matrix_create(20)
checker_matrix_print (checker)
       

check = checkerboard_create(20)
print(check)

