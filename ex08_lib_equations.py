import math


def linear_eq(a, b):
    if a == 0 and b != 0:
        result = 'Phương trình vô nghiệm'
    elif a == 0 and b == 0:
        result = 'Phương trình vô số nghiệm'
    else:
        result = -b/a
    return result


def quadrantic_func(a, b, c):
    if a == 0:
        linear_eq(b, c)
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            result = 'Phương trình vô nghiệm'
        elif delta == 0:
            result = 'Phương trình có nghiệm kép: x1 = x2 = ' + \
                str(round(-b/2*a, 2))
        else:
            result = 'Phương trình có hai nghiệm x1 = ' + \
                str(round(((-b + math.sqrt(delta))/(2*a)), 2)) + \
                ' x2 = ' + str(round(((-b - math.sqrt(delta))/(2*a)), 2))
    return result


a = eval(input('a = '))
b = eval(input('b = '))
c = eval(input('c = '))

kq = quadrantic_func(a, b, c)
print(kq)
