import sqlite3

conn = sqlite3.connect('python_nangcao/company.db')
sql_create_table = '''CREATE TABLE IF NOT EXISTS employee(
    ID_ INTEGER PRIMARY KEY,
    NAME TEXT NOT NULL,
    AGE INT,
    ADDRESS CHAR(50),
    SALARY REAL
);'''
conn.execute(
    sql_create_table)  # INTERGER PRIMARY KEY -> Tự tăng # INT PRIMARY KEY -> Không tự tăng #char từ 0 đến 255

sql_insert = '''INSERT INTO employee (NAME, AGE, ADDRESS, SALARY)\
    VALUES("Paul", 32, "California", 200000)'''
conn.execute(sql_insert)
sql_insert = '''INSERT INTO employee (NAME, AGE, ADDRESS, SALARY)\
    VALUES("Allen", 35, "Texas", 150000)'''
conn.execute(sql_insert)
sql_insert = '''INSERT INTO employee (NAME, AGE, ADDRESS, SALARY)\
    VALUES("Teddy", 23, "Norway", 200000)'''
conn.execute(sql_insert)
sql_insert = '''INSERT INTO employee (NAME, AGE, ADDRESS, SALARY)\
    VALUES("Mark", 25, "Rich-mond", 650000)'''
conn.execute(sql_insert)

sql_insert = '''INSERT INTO employee (NAME, AGE, ADDRESS, SALARY)\
    VALUES(?, ?, ?, ?); '''
conn.execute(sql_insert, ("Trung", 22, "Da Lat", 1200000000))

conn.commit()

conn.close()
