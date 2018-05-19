import math

s_circle = lambda r: math.pi * r ** 2
p_circle = lambda r: math.pi * r * 2

s_rectangle = lambda a,b: a * b 
p_rectangle = lambda a,b: 2* (a + b)

r = eval(input('Nhập bán kính hình tròn: '))
a = eval(input('Nhập chiều dài hình chữ nhật: '))
b = eval(input('Nhập chiều rộng hình chữ nhật: ')) 

print('Diện tích hình tròn:', round(s_circle(r), 2))
print('Chu vi hình tròn:', round(p_circle(r),2))

print('Diện tích hình chữ nhật:', s_rectangle(a, b))
print('Chu vi hình chữ nhật:', p_rectangle(a, b))