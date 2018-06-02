import sqlite3 

conn = sqlite3.connect('python_nangcao/company.db')

sql_read = '''SELECT * FROM employee;'''

data = conn.execute(sql_read)

for row in data:
    print('ID:', row[0])
    print('NAME:', row[1])
    print('AGE:',row[2])
    print('ADDRESS:', row[3])
    print('SALARY:', row[4])
    print('\n')

