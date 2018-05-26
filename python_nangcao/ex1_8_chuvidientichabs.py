from ex1_8_chuvidientichabs_lib import Triangle, Circle, Rectangle

dieu_kien = 1
while dieu_kien == 1:
    try:
        shape = int(input('Bạn muốn chọn hình nào? 1: Tròn, 2: Chữ Nhật, 3: Tam giác: \t'))
        assert (shape == 1 or shape == 2 or shape == 3)
        dieu_kien = 0
    except (AssertionError, ValueError):
        print('Loại hình không tồn tại, vui lòng nhập lại')
        dieu_kien = 1

if shape == 1:
    try:
        radius = eval(input('Nhập bán kính: \t'))
        assert radius > 0
    except AssertionError:
        print('Bán kính phải lớn hơn 0')
    except NameError:
        print('Bán kính phải là số')
    else:
        circle = Circle(radius)
        print('Chu vi = ', round(circle.cal_perimeter(),2))
        print('Diện tích = ', round(circle.cal_area(), 2))
elif shape == 2:
    try:
        length = eval(input('Nhập chiều dài: \t '))
        width = eval(input('Nhập chiều rộng: \t'))
        assert (length > 0 and width > 0)
    except AssertionError:
        print('Chiều dài và chiều rộng phải lớn hơn 0')
    except NameError: 
        print('Chiều dài và chiều rộng là số')
    else: 
        rect = Rectangle(length, width)
        print('Chu vi = ', rect.cal_perimeter())
        print('Diện tích = ', rect.cal_area())
else: 
    try:
        a = eval(input('Nhập cạnh a: \t'))
        b = eval(input('Nhập cạnh b: \t'))
        c = eval(input('Nhập cạnh c: \t'))
        assert (a + b > c and b + c > a and a + c > b)
    except AssertionError:
        print('Độ dài ba cạnh không hợp lệ')
    except NameError:
        print('Độ dài các cạnh là số')
    else:
        tria = Triangle(a, b, c)
        print('Chu vi = ', tria.cal_perimeter())
        print('Diện tích = ', tria.cal_area())