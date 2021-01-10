import pymysql

db = pymysql.connect('localhost', 'root', '1997', 'book_manager')

cursor = db.cursor()

cursor.execute('select * from book_info')

data = cursor.fetchone()

# print(f'Database version: {data}')
print(data)

db.close()