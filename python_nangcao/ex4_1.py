import sqlite3

class Product(object):
    def __init__(self, ID, name, price, amount):
        self.id = ID
        self.name = name
        self.price = price
        self.amount = amount

conn = sqlite3.connect('python_nangcao/ql_product.db')

"""
sql_create = ''' CREATE TABLE PRODUCT(
    ID INTEGER PRIMARY KEY,
    NAME TEXT NOT NULL,
    PRICE REAL NOT NULL,
    AMOUNT INT NOT NULL
); '''

conn.execute(sql_create)
"""

i = 1
while i == 1:
    job = int(input('Bạn muốn làm gì?\n \
                    1: Hiển thị danh sách sản phẩm \n \
                    2: Thêm sản phẩm vào bảng sản phẩm \n \
                    3: Tìm kiếm thông tin sản phẩm theo tên \n\
                    4: Cập nhật đơn giá và số lượng của một sản phẩm theo ID \n \
                    5: Xóa một sản phẩm theo ID \n'))
    if job == 1:
        sql_read = '''SELECT * FROM PRODUCT;'''
        data = conn.execute(sql_read)       
        for product in data:
            print('ID: ', product[0])
            print('Name', product[1])
            print('Price:', product[2])
            print('Amount:', product[3])
    elif job == 2:
        name = input('Nhập tên sản phẩm: ')
        price = eval(input('Nhập đơn giá sản phẩm: '))
        amount = int(input('Nhập số lượng sản phẩm: '))
        sql_add = '''INSERT INTO PRODUCT (NAME, PRICE, AMOUNT) \
            VALUES(?, ?, ?) '''
        conn.execute(sql_add, (name, price, amount))
        conn.commit()
        print('Đã thêm')
    elif job == 3:
        find_s = input('Nhập tên sản phẩm cần tìm: ')
        list_product = []
        sql_read = 'SELECT * FROM PRODUCT'
        data = conn.execute(sql_read)
        for product in data:
            ID = product[0]
            name = product[1]
            price = product[2]
            amount = product[3]
            prod = Product(ID, name, price, amount)
            list_product.append(prod)
        for product in list_product:
            if product.name.lower().find(find_s.lower()) != -1:
                print(product.id, '-', product.name, '-', product.price, '-', product.amount)
    elif job == 4:
        ID = int(input('Nhập ID: '))
        sql_select = '''SELECT * FROM PRODUCT WHERE ID =  ?'''
        data = conn.execute(sql_select, (ID,))
        price = eval(input('Nhập đơn giá mới \t'))
        amount = int(input('Nhập số lượng mới \t'))
        sql_update = '''UPDATE PRODUCT SET PRICE = ?, AMOUNT = ? WHERE ID = ?'''
        conn.execute(sql_update, (price, amount, ID))
        conn.commit()
        print('Đã cập nhật')
    elif job == 5:
        ID = int(input('Nhập ID: '))
        sql_delete = '''DELETE FROM PRODUCT \
                        WHERE ID = ?'''
        conn.execute(sql_delete, (ID,))
        print('Đã xóa')
    i = int(input('Tiếp tục? Tiếp: 1, Dừng:0 \t'))
conn.close()
