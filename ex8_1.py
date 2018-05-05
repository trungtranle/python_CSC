can_tup = ('Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỳ')
chi_tup = ('Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi')

def tinh_can (year):
    du = year % 10
    can = can_tup[du]
    return can

def tinh_chi (year):
    du = year % 12
    chi = chi_tup[du]
    return chi

nam = int(input('Nhập năm: \t'))

can = tinh_can(nam)

chi = tinh_chi(nam)

print(nam, 'là',can,chi)