import random

set1 = set()
set2 = set()

i, j = 1, 1

while i == 1:
    set1.add(int(input('Nhập giá trị thứ %d cho element trong set 1: ' %(len(set1)+1))))
    i = int(input('Tiếp tục nhập giá trị cho set 1? Yes: 1, No: khác 1 '))

while j == 1:
    set2.add(int(input('Nhập giá trị thứ %d cho element trong set 2: ' %(len(set2)+1))))
    j = int(input('Tiếp tục nhập giá trị cho set 2? Yes: 1, No: khác 1 '))

print('Set 1:', set1)
print('Set 2:', set2)
print('Chiều dài set 1:', len(set1))
print('Chiều dài set 2:', len(set2))
print('Tổng set 1', sum(set1))
print('Tổng set 2', sum(set2))
print('Max set 1: ', max(set1))
print('Max set 2: ', max(set2))
print('Pop set 1', set1.pop())
print('Set 1 sau pop', set1)
print('Set union', set1 | set2)
print('Set intersection', set1 & set2)
print('Set difference', set1 - set2)
print('Set symmetric difference', set1 ^ set2)
print('Set 1 tăng dần', sorted(set1))
print('Set 2 giảm dần', sorted(set2, reverse = True))