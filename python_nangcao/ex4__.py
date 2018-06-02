import sqlite3

conn = sqlite3.connect('python_nangcao/company.db')

cur = conn.cursor()

sql_update = '''UPDATE employee
                SET SALARY = ?
                WHERE ID_ = ?'''

cur.execute(sql_update, (1000000000000, 13))
#conn.execute(sql_update, (2000000000000, 13))

sql_delete = '''DELETE FROM employee
                WHERE ID_ = ? '''

cur.execute(sql_delete,(12,))

cur.execute('''DELETE FROM employee''')
conn.commit()

conn.close()