import sqlite3

conn = sqlite3.connect('python_nangcao/ql_nhan_vien.db')

"""sql_create_table_phong = '''CREATE TABLE PHONG (
    ID INTEGER PRIMARY KEY,
    TEN TEXT NOT NULL,
    CHUC_NANG TEXT NOT NULL
); '''

conn.execute(sql_create_table_phong)

sql_insert_1 = ''' INSERT INTO PHONG (TEN, CHUC_NANG)\
                VALUES('Hành chính','Giải quyết các công việc hành chính của công ty')'''
sql_insert_2 = ''' INSERT INTO PHONG (TEN, CHUC_NANG)\
                VALUES('Kỹ thuật','Thực hiện các dự án kỹ thuật của công ty')'''
conn.execute(sql_insert_1)
conn.execute(sql_insert_2)
conn.commit()
sql_create_table_nhanvien = ''' CREATE TABLE NHAN_VIEN (
    ID INTEGER PRIMARY KEY,
    HO_TEN TEXT NOT NULL,
    TUOI INTEGER NOT NULL,
    DIA_CHI TEXT NOT NULL,
    LUONG REAL NOT NULL,
    ID_PHONG INTEGER NOT NULL,
    FOREIGN KEY(ID_PHONG) REFERENCES PHONG(ID)
); '''
conn.execute(sql_create_table_nhanvien)
sql_insert = ''' INSERT INTO NHAN_VIEN(HO_TEN, TUOI, DIA_CHI, LUONG, ID_PHONG) \
        VALUES ('Trung', 21, 'Da Lat', 12000000, 2)'''

conn.execute(sql_insert)
conn.commit()

"""
i = 1
while i == 1:
    job = int(input('Chọn 1 trong các chức năng:\n \
                    1: Hiển thị danh sách phòng \n \
                    2: Thêm phòng mới \n \
                    3: Thêm nhân viên theo phòng \n \
                    4: Hiển thị danh sách nhân viên theo phòng \n'))
    if job == 1:
        sql_read = '''SELECT * FROM PHONG '''
        data = conn.execute(sql_read)
        for row in data:
            print('ID:', row[0])
            print('Tên phòng', row[1], '\n')
    if job == 2:
        name = input('Tên phòng mới: ')
        func = input('Chức năng phòng: ')
        sql_add = ''' INSERT INTO PHONG (TEN, CHUC_NANG)\
                    VALUES(?, ?) '''
        conn.execute(sql_add, (name, func))
        conn.commit()
        print('Đã thêm phòng')
    if job == 3:
        name = input('Tên nhân viên mới: ')
        tuoi = int(input('Tuổi: '))
        dia_chi = input('Địa chỉ: ')
        luong = eval(input('Lương: '))
        id_phong = int(input('ID Phòng: '))
        sql_insert = ''' INSERT INTO NHAN_VIEN(HO_TEN, TUOI, DIA_CHI, LUONG, ID_PHONG) \
                    VALUES (?, ?, ?, ?, ?)'''
        conn.execute(sql_insert, (name,tuoi,dia_chi,luong,id_phong))
        conn.commit()
        print('Đã thêm nhân viên')
    if job == 4:
        list_phong = []
        list_ten_phong = []
        sql_read = '''SELECT * FROM PHONG '''
        data = conn.execute(sql_read)
        
        for row in data:
            list_phong.append(row[0])
            list_ten_phong.append(row[1])
        for j in range(0, len(list_phong)):
            print('DS Nhân viên phòng', list_ten_phong[j])
            sql_read_2 = '''SELECT * FROM NHAN_VIEN WHERE ID_PHONG = ?'''
            data2 = conn.execute(sql_read_2, (list_phong[j],))


            for row in data2:
                print('ID:', row[0])
                print('Tên:',row[1])
                print('Tuổi:', row[2])
                print('Địa chỉ', row[3])
                print('Lương', row[4])
    i = int(input('Tiếp tục? Tiếp: 1, Dừng: 0 \t'))
conn.close()