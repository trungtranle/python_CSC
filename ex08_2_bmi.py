def bmi_cal_eval(weight, height):
    bmi = weight / (height ** 2)
    result = ''
    if bmi < 18.5:
        result = 'Gầy'
    elif bmi < 25:
        result = 'Bình thường'
    else:
        result = 'Thừa cân'
    return bmi, result


weight = eval(input('Nhập cân nặng (kg): '))
height = eval(input('Nhập chiều cao (m): '))

bmi, result = bmi_cal_eval(weight, height)
print('Chỉ số BMI:', round(bmi, 2))
print('Kết quả:', result)
